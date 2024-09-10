24/09/10
Google Calendar API를 이용해 달력을 불러오는 과정 추가중
https://developers.google.com/calendar/api/quickstart/python?hl=ko 를 참고해 같은 방식으로 이용자 계정의 token을 얻으려 했으나, 이후 배포 과정에서 credentials.json 내 클라이언트 정보에 대한 보안 문제가 확인되어 다른 방식을 고려하는 중

- Flask를 이용해 서버에서 OAuth 2.0 인증을 처리하는 방식으로 코드 재구성