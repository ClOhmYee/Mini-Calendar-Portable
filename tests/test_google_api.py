import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

import google_api

if __name__ == '__main__':
     google_api.test_ten_events(google_api.authenticate_google())