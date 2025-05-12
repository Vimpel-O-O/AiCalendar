from openai import OpenAI
import datetime
from config import CHATGPT_API_KEY

class EventParser():
    def __init__(self):
        # getting credentials from auth_data.py to use OpenAI API
        self.client = OpenAI(api_key=CHATGPT_API_KEY)
        # getting current date to set for AI
        self.now = datetime.datetime.now().isoformat()

    def parse_event(self, request):
        # Input format:
        response = self.client.responses.create(
            model="gpt-4o-mini",
            input="You are a parser. Extract fields: summary|startdatetime|enddatetime|description|location|recurrence|event_type\n" \
                "- Today's date to understand timing: " + self.now + "\n" \
                "- Dates must be ISO 8601 format (example: 2025-05-01T15:00:00-07:00)\n" \
                "- Location example might be: at college, in <name> cafe\n" \
                "- Recurrence must be DAILY or WEEKLY\n" \
                "- **IMPORTANT: summary, startdatetime, and enddatetime are ALWAYS REQUIRED. They can NEVER be NA.**\n" \
                "- For all other fields, if missing, use NA" \
                "- Description can be putted with text only when description keyword was said before that" \
                "- One of event types is required: SWE, Work, College, Important. SWE key word contains prep to software engineering role." \
                "If event type is not related to any of those use Other\n" \
                "- Output must be a single line with no quotes, no extra spaces, fields separated by |\n" \
                "- No commentary or explanation\n" \
                "- Remove all quotation marks\n" \
                "Request: " + request
        )
        event_info = response.output_text.split("|")
        return event_info
