from oauth2client.client import verify_id_token
from openpyxl import load_workbook # 파일 불러오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time

wb = load_workbook("Walmart PIckups GA Warehouse.xlsx") # Walmart PIckups GA Warehouse.xlsx 파일에서 wb 을 불러옴
ws = wb.active  # 활성화된 Sheet

"""
1. Google sheet download (Walmart PIckups GA Warehouse.xlsx) 

2. 빈 Load 번호 cell 정보 확인 
    2-1. [IF]: 빈칸이 있다면
        2-1-1. 빈 Load 번호 cell의 좌측 2컬럼 옆 PO 번호를 식별
        2-1-2. Walmart supplier 웹사이트에 접속
        2-1-3. ID, PW 정보 입력 로그인 버튼 클릭
        2-1-4. 상단 Supplier 메뉴 클릭
        2-1-5. Routing Tools 메뉴 클릭
        2-1-6. Routing Status 메뉴 클릭
        2-1-7. Search 메뉴에서 PO# or Load# 메뉴 클릭
        2-1-8. Search By PO Numbers 메뉴에 Load 번호가 없는 PO 번호 입력
        2-1-9. 하단의 Search 메뉴 클릭 

        
    2-2. [IF]: 빈칸이 없다면 
    
3. 

"""


Po_num = []  # Blank가 아닌 PO번호의 셀 정보를 담을 리스트 생성
Po_num_bl = [] # Blank인 PO번호의 셀 정보를 담을 리스트 생성


for x in range(2, 149):
    y=2
    verify=ws.cell(row=x, column=y).value #PO 넘버 컬럼의 값을 149low 까지 가져와 변수에 넣는다.
    if verify == None: #PO#가 null 아닐 경우
        #PO#의 셀 정보를 리스트에 넣는다. 
        Po_num.append(ws.cell(row=x, column=y))  #리스트 2번 부터 데이터 삽입 #셀의 정보
 

    elif verify != "": #PO번호가 null 일경우 
        Po_num_bl.append(ws.cell(row=x, column=y)) #Po_num_bl 리스트에 PO번호가 null인 셀의 정보를 순차 삽입
        #print(Po_num_bl) # 모든 Po_num_bl 리스트의 값을 출력 

print(Po_num)








