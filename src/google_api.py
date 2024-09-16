import os.path
import datetime

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
base_path = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(base_path, 'credentials.json')
token_path = os.path.join(base_path, 'token.json')

def authenticate_google():
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    return service

def get_picked_events(date):
    creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/calendar.readonly'])
    service = build('calendar', 'v3', credentials=creds)

    start_of_day = datetime.datetime.combine(date, datetime.time.min).isoformat() + 'Z'
    end_of_day = datetime.datetime.combine(date, datetime.time.max).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary',
                                                timeMin=start_of_day,
                                                timeMax=end_of_day,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return -1   # Events on that date do not exist
    else:
        return events
    

# just for test, modify next
def test_ten_events(service, max_results=10):
    now = datetime.datetime.now().isoformat() + "Z"
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get('items', [])
    
    if not events:
        print('No upcoming events found.')
        return
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
    
    return events

# test function for get all info from user, remove later or improve it
def list_calendars(self):
    
    calendar_list_result = self.service.calendarList().list().execute()
    calendars = calendar_list_result.get('items', [])

    for calendar in calendars:
        print(f"Summary: {calendar['summary']}, ID: {calendar['id']}")
