import os
import datetime
import sys
import encryption as enc

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
base_path = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(project_root, "data", "credentials.json")
token_path = os.path.join(project_root, "data", "token.json")

# this function makes both token.json and token_enc.json(encrypted token file)
# in main close event, only token_enc.json will remain safe, for security
def authenticate_google():
    creds = None
    enc_path = os.path.join(project_root, "data", "token_enc.json")
    

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0, prompt='consent')
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

        if os.path.isfile(token_path):
            enc.encryption(token_path)

    else:
        if os.path.isfile(enc_path):
            enc.decryption(enc_path)

        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    service = build('calendar', 'v3', credentials=creds)

    return service

def get_picked_events(date, utc_value):
    all_events = []
    service = authenticate_google()

    calendar_list_result = service.calendarList().list().execute()
    calendars = calendar_list_result.get('items', [])

    start_of_day = datetime.datetime.combine(date, datetime.time.min).isoformat() + utc_value
    end_of_day = datetime.datetime.combine(date, datetime.time.max).isoformat() + utc_value
    
    for picked_calendar in calendars:
        picked_calendar_id = picked_calendar['id']
        events_result = service.events().list(calendarId=picked_calendar_id,
                                                timeMin=start_of_day,
                                                timeMax=end_of_day,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
        events = events_result.get('items', [])

        if events:
            all_events.extend(events)

    return all_events
