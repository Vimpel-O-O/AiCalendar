from calendar_client import event_creation
from chatgpt_parser import event_parser
from app_gui import gui
import speech_recognition as sr
import tkinter as tk
from googleapiclient.errors import HttpError
from config import SWE_CALENDAR_ID, WORK_CALENDAR_ID, COLLEGE_CALENDAR_ID, IMPORTANT_CALENDAR_ID, OTHER_CALENDAR_ID

# Speech recognition setup
recognizer = sr.Recognizer()
mic = sr.Microphone()
# Adjust pause threshold to allow longer pauses
recognizer.pause_threshold = 2  # seconds
# Filter out background noise setting
recognizer.energy_threshold = 400

# Event creation audio request flow
def program_flow():
    # Audio request setup
    with mic as source:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=12)
    try:
        # Recognize the audio using Google Web Speech API
        request = recognizer.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        app.create_label("Sorry, I did not get the audio.", program_flow)
        return

    # Parse the event using EventParser
    event_prsr = event_parser.EventParser()
    event_info = event_prsr.parse_event(request)
        
    # in [summary, startdatetime, enddatetime, description, location, recurrence, event_type] format:
    summery = event_info[0] if event_info[0] != "NA" else ""
    startdatetime = event_info[1] if event_info[1] != "NA" else ""
    enddatetime = event_info[2] if event_info[2] != "NA" else ""
    description = event_info[3] if event_info[3] != "NA" else ""
    location = event_info[4] if event_info[4] != "NA" else ""
    if event_info[5] == "NA":
        recurrence = "RRULE:FREQ=DAILY;COUNT=1" # default to 1 day
    else:
        recurrence_rate = event_info[5] # DAILY or WEEKLY
        recurrence = "RRULE:FREQ=" + recurrence_rate + ";"

    # event format
    event = {
        'summary': summery,
        'location': location,
        'description': description,
        'start': {
        'dateTime': startdatetime,
        'timeZone': 'America/Los_Angeles',
        },
        'end': {
        'dateTime': enddatetime,
        'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        recurrence,
        ],
        'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
        ],
        },
    }

    # Set the event type
    if event_info[6] == "SWE":
        calID =  SWE_CALENDAR_ID
    elif event_info[6] == "Work":
        calID = WORK_CALENDAR_ID
    elif event_info[6] == "College":
        calID = COLLEGE_CALENDAR_ID
    elif event_info[6] == "Important":
        calID = IMPORTANT_CALENDAR_ID
    else:
        calID = OTHER_CALENDAR_ID

    # Create the event in Google Calendar
    event_crtn = event_creation.CalendarClient()
    try:
        event = event_crtn.create_event(calID, event)
        # Create a link label to the event
        event_url = event_crtn.get_url(event)
        app.create_link_label(root, "Event Created: " + request, event_url, program_flow)
    except HttpError:
        app.create_label("Bad Request error accured, try again.", program_flow)

# GUI setup
root = tk.Tk()
app = gui.AppGui(root)
app.create_button(program_flow)
root.mainloop()