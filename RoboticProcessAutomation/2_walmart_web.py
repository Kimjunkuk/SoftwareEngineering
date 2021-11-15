from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import pyperclip 


def walmart_login(): 
    #드라이버 로딩 
    driver = webdriver.Chrome('./chromedriver.exe') 
    
    #사용할 변수 선언 
    #url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/N3SUi/resume/as/authorization.ping' << 사용불가&로그인 불가 url 
    #url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/ie6cU/resume/as/authorization.ping' << 사용불가&로그인 불가 url
    url = 'https://retaillink2.wal-mart.com/TSCP2/?ukey=W6520'
    uid = '****' 
    upw = '****' 
    
    #Walmart 로그인 페이지로 이동 
    driver.get(url) 
    time.sleep(3)  #로딩 대기
    

    # find_element_by_id
    # find_element_by_name
    # find_element_by_xpath
    # find_element_by_link_text
    # find_element_by_partial_link_text
    # find_element_by_tag_name
    # find_element_by_class_name

    
    # 아이디 입력폼 Rev-1 >> tag_id = driver.find_element_by_id('uname') 
    # find_element_by_class_name 테그 안에 해당하는 문장을 인식하도록 설정
    tag_id =driver.find_element_by_css_selector("input[data-automation-id='uname']")
    
    #패스워드 입력폼 Rev-1 >> tag_pw = driver.find_element_by_id('pwd') 
    tag_pw =driver.find_element_by_css_selector("input[data-automation-id='pwd']")
    
    
    # id 입력 
    # # 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기 
    tag_id.click() 
    pyperclip.copy(uid) 
    tag_id.send_keys(Keys.CONTROL, 'v') 
    time.sleep(1) 
    
    # pw 입력 # 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기 
    tag_pw.click() 
    pyperclip.copy(upw) 
    tag_pw.send_keys(Keys.CONTROL, 'v') 
    time.sleep(1) 
    
    #로그인 버튼 클릭 
    login_btn = driver.find_element_by_css_selector("button[data-automation-id='loginBtn']")
    login_btn.click() 
    time.sleep(6) 
    
    # Supplier 버튼 클릭
    Supplier_btn = driver.find_element_by_id('transom-navbar-Supplier')
    if Supplier_btn != None: # 2-1-4-2. [IF]: Transportation Supply Chain Portal 2.0 접속이 되었다면 
        Supplier_btn.click() 
    else:
        Supply_Chain_btn = driver.find_element_by_link_text("Transportation Supply Chain Portal 2.0")
        Supply_Chain_btn.click() 
    time.sleep(4) 
    
    # Routing Tools 버튼 클릭
    Routing_Tools_btn = driver.find_element_by_id('twist-nav-Routing_Tools')
    Routing_Tools_btn.click() 
    time.sleep(2) 
    
    # Routing Status 버튼 클릭
    # a tag link_text를 직접 클릭할 수 있는 모듈 사용함
    Routing_Status_btn = driver.find_element_by_link_text("Routing Status")
    Routing_Status_btn.click() 
    time.sleep(2) 
    
    # PO# or Load# 버튼 클릭
    # PO_Load_btn = driver.find_element_by_css_selector("div[id='mat-tab-label-0-1']").click()
    PO_Load_btn = driver.find_element_by_id("mat-tab-label-0-1")
    PO_Load_btn.click() 
    time.sleep(100) 
    
    
    #체크 박스 클릭 
    # login_btn = driver.find_element_by_css_selector("input[type='checkbox']")
    # login_btn.click() 
    # time.sleep(1) 
    
    
    

    #로그인이 실패했을 경우 - 예: 아이디나 패스워드 불일치 
    # try: 
    #     #로그인 실패창 
    #     login_error = driver.find_element_by_css_selector('#err_common > div > p') 
    
    #     print('로그인 실패 > ', login_error.text) 
    
    # except: 
    #     print('로그인 성공') 
        
        
walmart_login()
