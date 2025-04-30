from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from config import GOOGLE_CREDENTIALS, GOOGLE_USER_TOKEN

class CalendarClient:
    def __init__(self):
        # access scope for calendar API
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]

    def get_credentials(self):
        try:
          # get saved google account credentials from token.json file
          creds = Credentials.from_authorized_user_info(GOOGLE_USER_TOKEN, self.SCOPES)

        except FileNotFoundError:
            # To generate token.json file with user credentials for the 1st time
            flow = InstalledAppFlow.from_client_config(GOOGLE_CREDENTIALS, self.SCOPES)
            creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
               token.write(creds.to_json())
        
        return creds

    def create_event(self, calID, event):
        service = build('calendar', 'v3', credentials=self.get_credentials())
        event = service.events().insert(calendarId=calID, body=event).execute()
        
        return "Event succesfully created: " + event.get('htmlLink')
    
    def get_url(self, url):
        url = url.split(" ")
        return url[-1]
        