from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from config import GOOGLE_CREDENTIALS, GOOGLE_USER_TOKEN
from google.auth.transport.requests import Request
from dotenv import set_key
import os
import sys
import google.auth.exceptions

class CalendarClient:
    def __init__(self):
        # access scope for calendar API
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]

    def restart_program(self):
        """Restarts the current Python program."""
        os.execv(sys.executable, [sys.executable] + sys.argv)

    def get_credentials(self):
        # get saved google account credentials from token.json file
        creds = Credentials.from_authorized_user_info(GOOGLE_USER_TOKEN, self.SCOPES)
        
        if creds.expired:
            # User goes through browser login
            flow = InstalledAppFlow.from_client_config(
                GOOGLE_CREDENTIALS,
                self.SCOPES
            )
            creds = flow.run_local_server(port=0)

            # Save new token to .env
            set_key(".env", "GOOGLE_USER_TOKEN", creds.to_json())
            self.restart_program()
        
        return creds

    def create_event(self, calID, event):
        service = build('calendar', 'v3', credentials=self.get_credentials())
        try:
            event = service.events().insert(calendarId=calID, body=event).execute()
        except google.auth.exceptions.RefreshError:
            creds = Credentials.from_authorized_user_info(GOOGLE_USER_TOKEN, self.SCOPES)
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            event = service.events().insert(calendarId=calID, body=event).execute()
        
        return "Event succesfully created: " + event.get('htmlLink')
    
    def get_url(self, url):
        url = url.split(" ")
        return url[-1]
        