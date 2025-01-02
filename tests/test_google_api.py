import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from src import google_api as api

if __name__ == '__main__':
    api.authenticate_google()
     # events = api.get_picked_events(api.datetime.date(2024,9,18))
     # if events == []:
     #     print('nothing')
     # else:
     #      for event in events:
     #           start = event['start'].get('dateTime', event['start'].get('date'))
     #           print(f"{start}: {event['summary']}")
