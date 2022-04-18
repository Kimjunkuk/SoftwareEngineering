1. ## [ SAP Macro work flow (Korean version)]

![inventorycount](https://user-images.githubusercontent.com/54308434/163850844-833d5b6d-e869-4eab-ac2d-9501e3d8981c.PNG)
![Sbin page](https://user-images.githubusercontent.com/54308434/163850857-74de51df-fea5-4e18-8891-d051b66ef773.PNG)
![Yes](https://user-images.githubusercontent.com/54308434/163850871-fdc52714-6669-4f83-8873-26560b613cae.PNG)

1.Sap_macro.py</br>

    1-1.workbook 불러오기
    1-1.workbook 활성화 

    1-1.Screen size >> 1920x1080 << 
    1-2.Windows 아이콘 위치로 마우스 커서 이동 Point(x=27, y=1052)
    1-3.Windows 아이콘 클릭
    1-4.SAP 검색 단어 클립보드에 복사
    1-5.SAP 검색 단어 붙여넣기
    1-6.Enter 입력 검색 결과 실행
    1-7.Enter 입력 SAP 로그인 화면 호출
    1-8.UserBox로 마우스 커서 이동: Point(x=289, y=279)
    1-9.Click UserBox
    1-10.SAP 계정 클립보드에 복사
    1-11.Paste User 정보
    1-12.PasswordBox로 마우스 커서 이동: Point(x=280, y=320)
    1-13.Click PasswordBox
    1-14.SAP 계정 패스워드 클립보드에 복사
    1-15.Paste User password 정보
    1-16.Enter 입력 SAP 로그인 
    1-17.SearchBox 로 마우스 커서 이동: Point(x=118, y=129)
    1-18.Click SearchBox
    1-19.SAP TCODE "ZWMR0224" 클립보드에 복사
    1-20.Paste User password 정보
    1-21.Enter 입력 SAP 로그인 
    
    
    1-22.S.Bin Box 로 마우스 커서 이동:  PointPoint(x=195, y=360)
    1-23.Click S.Bin Box
    1-24.시트로 부터 해당 x,y 값에 해당하는 컬럼의 데이터 가져옴
    1-25.시트로 부터 해당 x,y 값에 해당하는 컬럼의 데이터 복사
    1-26.복사된 데이터 S.Bin Box에 붙여넣기
    1-27.Enter 입력 S.Bin 실행
    1-28.Empty 로 마우스 커서 이동: Point(x=211, y=198)
    1-29.Click "Empty" Icon
    1-30.Yes 로 마우스 커서 이동: Point(x=139, y=356)
    1-31.Click "Yes" Icon

    1-32.Exit 아이콘으로 마우스 커서 이동:  Point(x=1886, y=16)
    1-33.Click "Exit" Icon
    1-34."Yes" 아이콘으로 마우스 커서 이동:  Point(x=350, y=614)
    1-35.Click "Yes" Icon

    오전 8시에 시작해서 3시간마다 쉬고 오후 8시까지 근무 하도록 