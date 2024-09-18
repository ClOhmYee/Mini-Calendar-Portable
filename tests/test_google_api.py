import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

import google_api as api

if __name__ == '__main__':
     events = api.get_picked_events(api.datetime.date(2024,9,18))
     if events == []:
         print('nothing')
     else:
          for event in events:
               start = event['start'].get('dateTime', event['start'].get('date'))
               print(f"{start}: {event['summary']}")
