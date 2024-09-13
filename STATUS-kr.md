# 프로그램 제작 과정 및 차후 진행 방향

## 24/09/10

Google Calendar API를 이용해 달력을 불러오는 과정 추가중

https://developers.google.com/calendar/api/quickstart/python?hl=ko 를 참고해 같은 방식으로 이용자 계정의 token을 얻으려 했으나, 이후 배포 과정에서 credentials.json 내 클라이언트 정보에 대한 보안 문제가 확인되어 다른 방식을 고려하는 중

##### - ~~Flask를 이용해 서버에서 OAuth 2.0 인증을 처리하는 방식으로 코드 재구성~~ 

## 24/09/13

Flask를 통한 서버 내 인증을 구현했으나, 이후 exe 프로그램 내 GUI에 표시하는 작업 중 access token의 데이터를 로컬에 저장해야 한다는 결론에 다다름. 결국 더 복잡하게 프로그램 구성을 하는 격이므로 이전 방식으로 재구성하고, 보안 위협에 관련된 최선책이 필요함

##### - credentials.json 압축 및 개인 access token 각 로컬 파일에 저장 방식 고려
