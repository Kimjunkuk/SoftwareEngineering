from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import pyperclip 

def google_download(): 
    #드라이버 로딩 
    driver = webdriver.Chrome('./chromedriver.exe') 
    
    #사용할 변수 선언 
    #url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/N3SUi/resume/as/authorization.ping' << 사용불가&로그인 불가 url 
    #url = 'https://retaillink.login.wal-mart.com/?resumePath=/as/ie6cU/resume/as/authorization.ping' << 사용불가&로그인 불가 url
    url = 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    uid = '****' 
    upw = '****' 
    
    uid1 = '****' 
    upw2 = '****' 
    
    driver.get(url) 
    time.sleep(5)  #로딩 대기
    
    # 아이디 입력폼 Rev-1 >> tag_id = driver.find_element_by_id('uname') 
    # find_element_by_class_name 테그 안에 해당하는 문장을 인식하도록 설정
    tag_id =driver.find_element_by_id("identifierId")
    
    # id 입력 
    # # 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기 
    tag_id.click() 
    pyperclip.copy(uid) 
    tag_id.send_keys(Keys.CONTROL, 'v') 
    time.sleep(3) 
    
    #Next 버튼 클릭 
    login_btn = driver.find_element_by_css_selector("button[jsname='LgbsSe']")
    login_btn.click() 
    time.sleep(100) 
    
    
google_download()

