from dotenv import load_dotenv
import os
import json

load_dotenv()  # This loads variables from .env into environment

CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

google_creds_str = os.getenv("GOOGLE_CREDENTIALS")
GOOGLE_CREDENTIALS = json.loads(google_creds_str)

google__user_token_str = os.getenv("GOOGLE_USER_TOKEN")
GOOGLE_USER_TOKEN = json.loads(google__user_token_str)

SWE_CALENDAR_ID = os.getenv("SWE_CALENDAR_ID")
WORK_CALENDAR_ID = os.getenv("WORK_CALENDAR_ID")
COLLEGE_CALENDAR_ID = os.getenv("COLLEGE_CALENDAR_ID")
OTHER_CALENDAR_ID = os.getenv("OTHER_CALENDAR_ID")