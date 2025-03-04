# 프로그램 제작 과정 및 차후 진행 방향

## 24/09/10

Google Calendar API를 이용해 달력을 불러오는 과정 추가중

https://developers.google.com/calendar/api/quickstart/python?hl=ko 를 참고해 같은 방식으로 이용자 계정의 token을 얻으려 했으나, 이후 배포 과정에서 credentials.json 내 클라이언트 정보에 대한 보안 문제가 확인되어 다른 방식을 고려하는 중

## 24/09/13

Flask를 통한 서버 내 인증을 구현했으나, 이후 exe 프로그램 내 GUI에 표시하는 작업 중 access token의 데이터를 로컬에 저장해야 한다는 결론에 다다름. 결국 더 복잡하게 프로그램 구성을 하는 격이므로 이전 방식으로 재구성하고, 보안 위협에 관련된 최선책이 필요함

##### - credentials.json 압축 및 개인 access token 각 로컬 파일에 저장 방식 고려 > 보안 중점으로!
#####  └ 실행 파일로 압축하는 과정에서 대부분 해소될 것으로 보이나, 개인 토큰은 배포 이후 각 이용자의 로컬에 저장되어 별도의 암호화 체계 고려중. 코드 추가만 하면 되는 부분으로 예상되어 차후 작업 예정

## 24/09/16

달력에서 특정 날짜를 클릭하면, 해당 날에 존재하는 스케줄을 Google Calendar에서 불러와 알맞게 팝업창으로 표시함. 팝업창 크기 및 위치에 대한 고려가 필요하며, primary 이외 다른 캘린더에 대한 정보도 불러오도록 추가 작업이 필요함

## 24/09/18

팝업창의 위치 조정(인스턴스화 포함)을 완료하고, 이용자 소유의 Google Calendar ID를 모두 가져와 확인하는 방식으로 코드를 추가함. 또한, token이 존재하지 않을 때 갱신하는 작업도 우선 포함했음. 대략적인 목표는 달성했지만, 여러 캘린더 목록을 불러오다보니 몇 배로 딜레이가 늘어 비동기 작업 등 여러 다른 방식을 적극 고려중

## 24/09/21

이용자의 위치에 따른 UTC 조정 클래스를 sub_utc_localization.py에서 구현중. 기초 구현은 test 결과 양호하지만, 이후 값을 어떻게 이용할지 타 클래스와의 조정 필요. main_calendar.py 내 가독성과 유지보수성을 고려해 추가 함수로 구조에 약간의 변화를 주었으며, 이후에도 각 클래스 간의 coupling 등 소프트웨어 설계에 연속된 체크 필요

## 24/09/28

메뉴바를 통한 UTC Localization 기능 접근 경로를 만들고, 해당 기능을 통해 값 지정 시 값을 메인 프레임에 저장해 주어진 값으로 일정 탐색을 하도록 구성함. 

## 24/09/30

인증 만료된 token을 refresh하는 코드가 정상 작동하지 않아 Google 계정의 재인증을 받아 token.json을 덮어쓰는 방식으로 채택함. 해당 방식이 다른 예외에도 유연하게 대처할 것으로 판단되므로 적당한 해결책이라고 생각함. 기능 추가를 위해서는 딜레이에 대한 분석과 개선이 우선이라고 판단됨.

## 24/10/06

일정이 있는 날의 배경을 바꾸어 가시성을 올리는 과정을 추가함. 프로그램 내 표시하고 있는 달에 전체의 일정을 한 번에 불러와 저장하는 구조로 변경을 계획중. 별도의 .json 파일을 추가하게 될 것이며, 한달 간 데이터를 로컬로 저장해 불러오는 방식을 채택하는 방식이 딜레이 개선 및 다른 기능에도 긍정적인 영향을 줄 것으로 예상됨.

## 24/10/28

##### 1. 현재 보이는 달의 데이터 전체를 불러와 저장할 때

한 달 간의 데이터를 가져오는 것부터 매우 스케일이 큰 작업으로, 일정 수와 당시 환경 등 이용자에 따라 매우 큰 딜레이가 발생될 것으로 예상됨.

##### 2. 일정의 업데이트가 필요할 때

업데이트 버튼을 추가해 이용자가 원할 때 다시 한 번 불러오는 작업을 하도록 구성할 수 있으나, 1번의 문제와 더불어 이미 존재하는 일정의 데이터는 덮어쓰지 않는 등 효율적인 알고리즘 구상이 필요하다고 판단함.


크게 두 가지의 문제의 해결이 쉽지 않을 것이라 판단해, 우선 token을 encrypt하는 메커니즘을 만들어보는 것으로 방향을 전환함.

## 25/01/02

추가적으로 달의 데이터를 불러와 로컬에 저장하는 방식을 채택할 시, 그 저장 데이터에 개인의 사생활이 담겨있기 때문에 보안 문제가 예상됨. 그러므로 추가적인 작업을 통해 방대한 양의 데이터를 암호화해야 하는데, 이 경우 더 많은 딜레이가 소요되므로 많은 생각 후에 로컬에 저장하는 방식을 사용하지 않도록 결정함.

authentication 파일(token 등)은 로컬에 저장되므로, 해당 파일에만 암호화를 진행하는 코드를 추가할 예정임.

#### authentication 파일 encryption 코드 추가