from dotenv import load_dotenv
import os
import json
import sys

# Determine base path (where .env resides)
if getattr(sys, 'frozen', False):  # Running as PyInstaller bundle
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

dotenv_path = os.path.join(base_path, '.env')
load_dotenv(dotenv_path=dotenv_path)  # This loads variables from .env into environment

CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

google_creds_str = os.getenv("GOOGLE_CREDENTIALS")
GOOGLE_CREDENTIALS = json.loads(google_creds_str)

google__user_token_str = os.getenv("GOOGLE_USER_TOKEN")
GOOGLE_USER_TOKEN = json.loads(google__user_token_str)

SWE_CALENDAR_ID = os.getenv("SWE_CALENDAR_ID")
WORK_CALENDAR_ID = os.getenv("WORK_CALENDAR_ID")
COLLEGE_CALENDAR_ID = os.getenv("COLLEGE_CALENDAR_ID")
OTHER_CALENDAR_ID = os.getenv("OTHER_CALENDAR_ID")