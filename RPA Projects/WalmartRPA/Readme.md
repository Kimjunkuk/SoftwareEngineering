### 1. Results
</br>
<table>
  <tr>
    <th>Location Label RPA results image</th>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/54308434/152708813-8c7b7899-d7de-4d4f-a0ac-0d9c723c6c60.png" alt="image1-1"></td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/54308434/152708821-2ea06bba-5efd-45d5-9200-d64cfe48ad1a.png" alt="image1-2"></td>
  </tr>
</table>

## [ Project info (Korean version)]

    1-1.공지 사항
        1-1-1.작업 시간
        1-1-1-1.총 작업 시간: 46 (Hours)
        1-1-1-2.종합 개선 작업 시간: 14 (Hours)
        1-1-1-3.종합 검토 작업 시간: 3 (Hours)  
        1-1-1-4.종합 개발 작업 시간: 29 (Hours)

## [ Important Notice (Korean version)]
### 1.변경되지 않는 고정변수명 모두 대문자 표기
### 2.모든 변수명 소문자 스네크 케이스 표기
### 3.클래스 캐멀 케이스 표기
<br><br>

## [ Start Setting (Korean version)]

1.Location setting

    1-1.CLIENT_SECRET_FILE = '파일 경로 확인 및 변경'
    1-2.GOOGLE_SHEET_ID = 'Walmart 마스터 구글 시트 ID 또는 PO번호를 추출할 대상 구글 시트 ID'
    1-3.wb = load_workbook("다운 받은 구글 시트의 첫번째 시트의 경로로 변경")
    1-4.wb.save("다운 받은 구글 시트의 첫번째 시트를 저장할 경로로 변경")
    1-5.driver = webdriver.Chrome('구글 크롬 드라이버 저장 경로로 변경')
    1-6.url = '월마트 포털 접속 URL 주소 입력 (주소 변경 X)'
    1-7.uid = '월마트 포털 접속 ID 입력'
    1-8.upw = '월마트 포털 접속 ID의 PW입력'
    1-9.path = "프로그램이 동작할 컴퓨터의 다운로드 폴터 경로로 변경"
    1-10.gc = pygsheets.authorize(service_file='구글 API 접속 keys.json 파일 경로로 변경')
    1-11.wb.save("다운 받은 구글 시트의 첫번째 시트를 저장할 경로로 변경")
    1-12.wb.save("다운 받은 구글 시트의 첫번째 시트를 저장할 경로로 변경")
    1-13.sender_address = '이메일 발송 계정의 ID로 변경'
    1-14.sender_pass = '이메일 발송 계정의 PW 변경'
    1-15.receiver_address = ['이메일을 받을 분의 주소로 변경', '이메일을 받을 분의 주소로 변경', ... ] 
    1-16.wb.close("프로그램 구동을 위해 다운 받았던 모든 엑셀 파일 의 경로로 변경")
    1-17.[os.remove(f) for f in glob.glob('프로그램 구동을 위해 다운 받았던 구글 엑셀 파일 의 경로로 변경')]
    1-18.[os.remove(f) for f in glob.glob('프로그램 구동을 위해 다운 받았던 월마트 엑셀 파일 의 경로로 변경')]
    1-19.[os.remove(f) for f in glob.glob('프로그램 구동을 위해 다운 받았던 모든 엑셀 파일 의 경로로 변경')]


## [ Library list in use (Korean version)]

    1.pygsheets: 구글 시트 제어 패키지
    2.openpyxl : 로컬 구글 시트 제어 패키지
    3.selenium : 컴퓨터 동작 제어 패키지
    4.time: 시간 제어 모듈
    5.pyperclip: 복사 붙여넣기 기능 제어 패키지
    6.pyautogui: 키보드 마우스 제어 패키지 (미사용 중)
    7.time: 시간 데이터 제어 모듈
    8.os: 운영 체제 인터페이스 제어
    9.Google: 구글 API 클래스 호출
    10.pandas: 데이터 제어 패키지
    11.glob: 파일 경로 제어 패키지
    12.smtplib:
    13.email.mime.multipart import MIMEMultipart: 모듈
    14.email.mime.text import MIMEText:

## [ Extra Documents ]
1.VS Code & Git SOP Location: Google Drive > Shared drives > ZINUS_McD > IT</br></br>

2.Walmart RPA project SOP location: Google Drive > Shared drives > ZINUS_McD > IT > Walmart RPA project</br></br>

3.Walmart RPA project task history list Location: Google Drive > Shared drives > ZINUS_McD > IT > Walmart RPA project

## [ Resources ]

1.Python website: https://www.python.org/</br></br>

2.Google user Credentials: https://console.cloud.google.com/projectselector2/apis/credentials?hl=ko&_ga=2.167447614.-1289008455.1563620716&pli=1&supportedpurview=project</br></br>

3.pygsheet : https://medium.com/game-of-data/play-with-google-spreadsheets-with-python-301dd4ee36eb</br></br>

## [ RPA operate flow (Korean version)]

1.Google.py</br>

    1-1.Google API 접속 클래스


2.main.py</br>

    2-1.Google API Client_secret.json 파일 경로
    2-2.API service 명 (기본값 변경 X)
    2-3.API service 버전 (기본값 변경 X)
    2-4.Goole API 계정의 업무 범위 설명 (구글 시트, 구글 슬라이드, 구글 워드 등등 사용할 구글 클라우드 소프트웨어 지정)
    2-5.Google Sheets ID 정보 
    2-6.Google 클래스의 Create_Service 함수 호출 및 매개변수 전달
    2-7.작업을 수행하고자 하는 Google sheets ID service.spreadsheets() 함수로 전달
    2-8.작업을 수행하고자 하는 Google sheet의 sheet들을 인자 값으로 받아 sheets에 저장 
    2-9.Google 시트를 sheet별로 분할하여 csv 파일 형식으로 다운로드 진행
    2-10.구글 마스터 시트로 부터 다운받은 시트에서 작업을 하고자 하느 시트의 해당이름의 csv파일을 읽어옴
    2-11.읽어온 파일을 csv 파일 형식에서 xlsx형식으로 변환후 저장할 파일의 이름
    2-12.xlsx 파일로 변환
    2-13.xlsx 파일로 저장
    2-14.데이터 제어 패키지 호출
    2-15.데이터 정재 작업이 필요한 파일 호출
    2-16.PO # 컬럼 기준으로 오름 차순 정렬 
    2-17.PANDAS 패키지를 사용하여 ('Sheet1.xlsx') 명의 파일로 재생성 쓰기
    2-18.Load 번호가 없는 PO 번호 전역 리스트 선언
    2-19.다운로드 받은 Google Master sheets 파일을 선언된 경로로 부터 wb로 불러옴
    2-20.불러온 wb 시트 활성화
    2-21.활성화된 시트의 B컬럼의 폭을 25px로 수정함
    2-22.활성화된 시트의 A컬럼의 폭을 25px로 수정함
    2-23.수정이 완료된 활성화시트 선언된 경로로 저장
    2-24.Load 번호 컬럼이 빈칸이지 않은 PO번호의 전역 리스
    2-25.Load 번호 컬럼이 빈칸인 PO번호의 전역 리스트
    2-26.다운로드 받은 Google Master sheets 파일로 부터 Load번호가 없거나 PO번호가 None이 아닌 PO번호들을 리스트에 적재함
    2-27.Load번호가 없거나 PO번호가 None이 아닌 경우를 식별함
    2-28.다운로드 받은 Google Master sheets 파일 에서 PO컬럼의 값이 공란인 셀을 확인할 경우 작업을 종료함
    2-29.다운로드 받은 Google Master sheets 파일 에서 Load번호가 있거나 PO번호가 None인 경우를 식별함
    2-30.다운로드 받은 Google Master sheets 파일로 부터 Load번호가 없거나 PO번호가 None이 아닌 PO번호들을 추출한 리스트로 부터 None값을 제거 한다
    2-31.다운로드 받은 Google Master sheets 파일로 부터 Load번호가 없거나 PO번호가 None이 아닌 PO번호들을 추출한 리스트로 부터 정재된 값을 추출하여 PO_num_li 명으로 선언된 리스트에 순차적으로 적재한다
        2-31-1.print(Lod_num_bl) # None 인 모든 셀 정보 출력, print(Lod_num) # None이 아닌 모든 셀 정보 출력
    2-32.Load 번호가 없는 모든 PO번호 오름차순 정렬 #print("Load 넘버가 없는 모든 PO번호:" + str(PO_num_li))  # Load 넘버가 없는 모든 PO번호 출력
    2-33.Google.exe 드라이버 호출
    2-34.접속 웹사이트 URL 선언 
        2-34-1.#url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/N3SUi/resume/as/authorization.ping' << 사용불가&로그인 불가 url
        2-34-2.#url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/ie6cU/resume/as/authorization.ping' << 사용불가&로그인 불가 url
    2-35.접속 웹사이트 로그인 ID
    2-36.접속 웹사이트 로그인 PW
    2-37.선언된 URL 주소의 웹사이트로 이동
    2-38.만약 로딩 페이지의 값이 None이 아닐 경우
    2-39.오류 발견시 웹 브라우저 종료
    2-40.아이디 입력폼 Rev-1 >> tag_id = driver.find_element_by_id('uname') find_element_by_class_name 테그 안에 해당하는 문장을 인식하도록 설정
    2-41.패스워드 입력폼 Rev-1 >> tag_pw = driver.find_element_by_id('pwd')
    2-42.크롬 브라우저 새로고침 중지
    2-43.입력폼 클릭
    2-44.uid 내용 복사
    2-45.uid 내용 붙여넣기
    2-46.1초 대기
    2-47.입력폼 클릭
    2-48.upw 내용 복사
    2-49.upw 내용 붙여넣기
    2-50.1초 대기
    2-51.로그인 버튼 클릭
    2-52."transom-navbar-Supplier" 요소가 로드될때 까지 최대 30초 대기 후 "transom-navbar-Supplier" 요소확인시 브라우저 종료
    2-53.Supplier 버튼 클릭
    2-54.Transportation Supply Chain Portal 2.0 접속이 되었다면 Supplier 버튼 클릭
    2-55.만약 메인 포털 사이트로 접속 될 경우 "Transportation Supply Chain Portal 2.0"를 포함하는 아이콘을 클릭
    2-56.Routing Tools 버튼 클릭
    2-57.Routing Status 버튼 클릭 a tag link_text를 직접 클릭할 수 있는 모듈 사용함
    2-58.PO# or Load# 버튼 클릭 PO_Load_btn = driver.find_element_by_css_selector("div[id='mat-tab-label-0-1']").click()
    2-59.Walmart PO번호 입력
    2-60.SEARCH 버튼 클릭
    2-61.Export 버튼 클릭
    2-62.로그 아웃 
    2-63.웹 브라우저 종료
    2-64.선언된 폴더 경로의 폴더로 부터 파일 이름 리스트 확보
    2-65.파일중 엑셀파일 리스트 얻기
        2-65-1.len_num = len(exfile_list)-1  # 항상 가장 마지막에 다운 받은 엑셀 파일기준으로 작업
        2-65-2.emp = pd.read_excel(str(path+"/"+excelfilename))  # 가장 최근에 받은 파일 활성화
        2-65-3.data.to_excel(str(path+"/"+excelfilename), index=False)  # 인덱스 값 없이 저장
    2-66.월마트 포털로 부터 다운받은 엑셀 파일을 식별 하여 호출함
    2-67.PO번호 검색결과 다운로드 받은 시트의 컬럼 14번의 값이 23234118과 같지 않을경우 row를 삭제하여라 모든 row를 확인 다 했다면 저장 후 작업을 종료하여라
        2-67-1.if str(num_check) != '23234118': # 변수를 Srting 설정하지 않을 경우 같은 값도 다르게 처리함
        2-67-2.ws1.delete_rows(q)  # Ship point 23234118과 값이 다른 Row를 삭제 처리
    2-68.월마트 포털로 부터 다운받은 엑셀에서 PO컬럼의 데이터가 적재된 데이터 전역 리스트
    2-69.구글 마스터 시트로 부터 다운받은 엑셀에서 PO컬럼의 데이터가 적재된 데이터 전역 리스트
    2-70.월마트 포털로 부터 다운받은 엑셀에서 PO컬럼의 데이터가 적재된 데이터 전역 리스트를 구글 시트와 비교 하기위해 사용함
    2-71.구글 마스터 시트로 부터 다운받은 엑셀에서 PO컬럼의 데이터가 적재된 데이터 전역 리스트를 월마트 시트와 비교 하기 위해 사용함 
    2-72.Walmart 포털에서 다운 받은 데이터의 수량 확인
    2-73.Google 포털에서 다운 받은 데이터의 수량 확인
        2-73-1.print('Importante message:: Walmart download data total: [ '+str(len(walmart_count_data_total))+' ] || Google Master sheets data total: [ '+str(len(google_count_data_total))+']')
        2-73-2.print('Walmart PO: '+str(walmart_count_data_total))
        2-73-3.print('Goolge PO: '+str(google_count_data_total))
    2-74.파악한 수량의 값이 일치할 경우 데이터 업데이트 작업 수행
    2-75.데이터 컬럼별 식별 작업 실시
    2-76.Po_num_li ( 구글에서 다운 받은 시트의 Load번호가 없는 PO의 리스트 )의 길이 만큼 반복 작업
    2-77.월마트 포털에서 다운 받은 엑셀시트에서 Po 번호 컬럼의 값이 PO_num_li[u]리스트상(Load번호가 없는 PO번호)에 있는 Po번호가 같은지를 식별하여 연산 수행
    2-78.중복 PO시 Load정보 공란 파악 구간, 구글에서받은원본엑셀시트 PO_num_li[5]의 값이 PO_num_li[4]같은데 월마트 포털에서 받아온 값의 Load번호 값이 비어 있다면 PO_num_li[5]를 건너뛰고 PO_num_li[6] 진행
    2-79.Load번호가 없는 PO번호 리스트의 값과 구글에서 다운로드 받은 파일에서 PO번호의 값이 같다면 && 로드 컬럼의 값이 비어 있다면
        월마트 포털로 부터 다운로드 받은 엑셀의 데이터를 추출하여 가져오는 구간
        2-79-1.index = ws1.cell(row=l, column=2).value # 다운로드 받은 엑셀파일의 Load 컬럼 값
        2-79-2.index_destination = ws1.cell(row=l, column=5).value # 다운로드 받은 엑셀파일의 Destination 컬럼 값
        2-79-3.index_Cases_DOQTY = ws1.cell(row=l, column=16).value# 다운로드 받은 엑셀파일의 DO Qty 컬럼 값
        2-79-4.index_Pallets = ws1.cell(row=l, column=19).value# 다운로드 받은 엑셀파일의 Pallets 컬럼 값
        2-79-5.index_PU_date = ws1.cell(row=l, column=9).value# 다운로드 받은 엑셀파일의 PU date 컬럼 값
        2-79-6.index_carrier = ws1.cell(row=l, column=11).value# 다운로드 받은 엑셀파일의 Carrier 컬럼 값
        2-79-7.index_SCAC = ws1.cell(row=l, column=12).value# 다운로드 받은 엑셀파일의 SCAC 컬럼 값
    2-80.구글 API 인증
    2-81.추출 정재 작업이 완료한 값을 넣어줄 구글 시트 이름
    2-82.첫번째 시트 선택
    2-83.DO Qty, Pallets 의 +-10% 공 차 범위 연산 구간
    2-84.구글원본 시트에서 가져온 DOQty값
    2-85.구글원본 시트에서 가져온 Pallets값
    2-86.구글 마스터 시트의 DOQty가 +-10% 공차 범위에 들어 오거나 Pallets가 +-10% 공차 범위에 들어 오거나 공란이 아닐 경우 경우 작업 수행
        2-86-1.ws.cell(row=z, column=4, value=str(index))  # 빈 Load cell 값 적재
        2-86-2.ws.cell(row=z, column=13, value=str(index_destination))  # Destination 셀 값 적재
        2-86-3.ws.cell(row=z, column=16, value=str(index_PU_date))  # PU date 셀 값 적재
        2-86-4.ws.cell(row=z, column=14, value=str(index_carrier))  # carrier 셀 값 적재
        2-86-5.ws.cell(row=z, column=15, value=str(index_SCAC))  # SCAC 셀 값 적재
    2-87.구글 마스터 시트의 DOQty가 +-10% 공차 범위에 들어 오거나 Pallets가 +-10% 공차 범위에 들어 오지 않거나 공란일 경우 작업 수행
    2-88.셀 배경 색상 변경 (Red, Green, Blue, Alpha)
    2-91.만약 Po컬럼의 값이 None이면 무한 루프 종료
    2-92.Walmart 포털에서 다운 받은 데이터의 수량과 Google 시트로 부터 다운 받은 데이터가 다른 번호 식별
    2-93.발송할 메일의 내용
    2-94.메일을 발송할 계정의 정보
    2-95.메일을 수령할 사람들의 이메일 주소
    2-96.MIME 구성 구간
    2-97.메일 제목 정보
    2-98.첨부 파일
    2-99.메일을 발송하기 위한 SMTP session 생성



## [ VS code Useful shortcut ]

ctrl+K+C: 선택 주석 </br>
ctrl+k+u: 선택 주석 해지 </br>
ctrl+k+f: 선택 자동 정렬 </br>


## [ Meeting logs ]

    Walmart RPA project 12/30/21 추가 개선사항 명세서
    1.RPA 사용 중인 메일을 기업 메일로 변경할 수 있도록 핼프데스크 측의 문의 하여 기업메일로 변경할것  (SMTP)
    2.이메일을 보낸 값을 제외한 나머지는 연산을 할 수 있도록 할것 
    3.DOQty, Pallets 수량이 10% 공차 범위 이내에 들어 올때 로드번호를 넣어주고 아닐 경우에는 값은 넣지 않고 붉은 색으로 표기할것 
    4.스캐줄러 어떻게 할 것 인지? 
    5.로직이 멈추면 개발자에게 어떻게 안내를 보낼 것 인지 예외사항 조치할것 (메일 and 문자 메시지 )
    6.위의 개선사항 명세서의 명시된 내용들을 기반으로 정확함 지속가능한 프로그램 개발 할것 
    

    Walmart RPA project 12/29/21 추가 요구사항 명세서
    1. DO와 PO는 월마트에포털에서 다운로드 받은 데이터에 DO값이 없기 때문에 쌍으로 묶는 것은 무의미함으로 쌍으로 묶어 처리하지 않음
    2. PO 컬럼의 PO번호 개수 기준으로 데이터 총 수량이 월마트 포털에서 가져온 값이랑 상이할 경우 경고 알림 메일을 운영인원에게 보내고 RPA는 아무 동작도 하지 않도록 구현할 것
    3. 경고 알림 메일에는 오류를 발생시킨 데이터의 정보를 포함한다. 누락된 (load 번호 또는 누락된 PO번호 정보)
    4. DO Qty, Pallets 수량이 ±10% 공차 범위 이내에 들어오지 않을 경우 기존의 Load 컬럼의 배경색을 붉은색으로 표기하도록 한다.
    5. DO Qty, Pallets 수량이 ±10% 공차 범위 이내에 들어오지 않을 경우에도 Load 번호를 비롯한 데이터 값들을 넣어준다. 

    Amazon RPA project 12/29/21요구사항 명세서
    1. 분산된 데이터를 메일로 부터 취합하는 시스템 구축
    ===============
    Walmart RPA project 12/xx/21 요구사항 명세서</br>
    PO 번호 중복 값에 대해서 Load 번호가 1개만 업데이트 되어있을때
    Load번호가 어떻게 삽입 되는가? 

    CP: 중간에 모았다가 배송지로 이동
    DC: 바로 배송지로

    다운받은 엑셀 파일 정렬시 PO번호 기준으로 정렬과 함꼐 Load번호 정렬도 함께 할것

    ===============
    12/03/21
    1. 미팅 질문
    1-1. 지난 MADB 기준으로 완료된 정보들을 다른 시트에 옮겨 통합 보관 가능 유무.
    1-1. [오찬영님] 지누스 측에서 같이 보기때문에 한개의 시트로 관리되어야 한다 
    1-2. [구철진님] 데이터량이 늘어 나게 되면 과거 데이터는 추가 시트에 보관(DB시트)

    2. 차기 프로젝트
    2-1. [1순위] Amazon RPA project
    2-2. [2순위] Google sheet macro
    2-3. [3순위] CJ Food Excel sheet  : 현장 작업자들에게 구체적인 작업지시 목적으로 사용예정
    2-3. [개발중] 최성철님 KPI
    2-4. [개발중] 비용관리(CPP) 시트
    2-5. Scott KPI 가장 후 순위 작업

    3. 미팅 내용
    3-1. [윤희권님] 기존 데이터에 데이터가 맞게 잘 적재 되는지 검증 작업 수행 하여 2차 미팅 준비할것
    3-1-1. 결과 중심 내용, 작업 완료 시간, ROI 산출

    3-2. [오찬영님] SAP 자동화 프로그램이 SAP에 접근할 수 있는 우회 경로 파악
    3-3. [구철진님]
    3-3-1오찬영님과 밀착 업무 진행 RPA
    3-3-2. 2022 1월에 Walmart 물량 진행에 실제 운영 적용 이후 정상 운영시 지누스 측에 보고하여 적용 예정
    3-3-3. CJ Food 이메일 에서 완전히 컨펌된 데이터를 가져와서 시트에 넣을 수 있는지 확인 요청
    3-3-4. CJ Food 야드 관리 프로그램이 중요해질 예정인데 웰컴센터 CS인원에게 모든 트럭 IN/out에 대해서 관리할 수 있는 툴 제작 건의, 해당 CS인원은 트럭이 Dock몇번으로 가면 업무가 원활히 진행 될 수 있는 판단 하는 목적으로 사용예정
    3-3-5. 야드 체크를 물리적으로 사람이 트레일러정보 컨테이너 정보가 적재 상태 인지 빈 상태 인지 관리해야하는 어려움을 개선할 수 있는 방안 모색
    3-3-6. WMS, YMS 모두 아우를 수 있는 물류 업무로 거듭날 수 있어야함

    ===============
    Walmart Pickups GA Warehouse << google sheet
    빨간색 컬럼만 업데이트 함
    흰색은  공란
    PO넘버를 월마트 포털에 가서 검색한다음
    로드 아이디를 찾고 스프레드 시트에 로드아이디를 업데이트
    흰색으로 표기된 공란의 컬럼에도 업데이트를 해준다.
    그다음에 케리어 측에서 연락이 오는데
    이메일에 픽업이(픽업리퀘스트 PU request) 가능한 시트에 입력하여 픽업 시간을 알려준다.
    커뮤니케이션을 통해 확정된 날자를
    Original appt date 컬럼에 입력
    그리고 재 일정 조정이 이루어진 날짜는 옆에 재일정컬럼에 입력 전일 발생한 쉽핑 애러는

