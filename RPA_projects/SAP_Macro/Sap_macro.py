from tkinter import Y
import pyautogui 
import pyperclip
import time
from openpyxl import load_workbook

wb = load_workbook("./RPA_projects/SAP_Macro/SBins.xlsx") # 2-24
ws = wb.active  # 2-25

def start_up():
    pyautogui.moveTo(27, 1052) # 1-2
    time.sleep(2)
    pyautogui.click() # 1-3
    time.sleep(2)
    pyperclip.copy("SAP") # 1-4
    pyautogui.hotkey('ctrl', 'v') # 1-5
    time.sleep(2)
    pyautogui.press('enter') # 1-6
    time.sleep(2)
    pyautogui.press('enter') # 1-7
    time.sleep(2)
    pyautogui.moveTo(289, 279) # 1-8
    time.sleep(2)
    pyautogui.click() # 1-9
    time.sleep(2)
    pyperclip.copy("E00145") # 1-10 E00127
    pyautogui.hotkey('ctrl', 'v') # 1-11
    pyautogui.moveTo(280, 320) # 1-12
    pyautogui.click() # 1-13
    pyperclip.copy("Cjl0125!") # 1-14 Cjl011722!
    pyautogui.hotkey('ctrl', 'v') # 1-15
    time.sleep(2)
    pyautogui.press('enter') # 1-16
    time.sleep(2)
    pyautogui.moveTo(118, 129) # 1-17
    pyautogui.click() # 1-18
    pyperclip.copy("ZWMR0224") # 1-19
    pyautogui.hotkey('ctrl', 'v') # 1-20
    pyautogui.press('enter') # 1-21

def empty_bin_macro_start():
    pyautogui.moveTo(208, 358) # 1-22
    pyautogui.click() # 1-23

    x=1
    y=1
    while True:
        verify = ws.cell(row=x, column=y).value # 2-24
        if verify != None:
            print(str(verify))
            time.sleep(2)
            pyperclip.copy(verify) # 1-25
            pyautogui.hotkey('ctrl', 'v') # 1-26
            pyautogui.press('enter') # 1-27
            time.sleep(2)

            pyautogui.moveTo(211, 198) # 1-28
            pyautogui.click() # 1-29
            time.sleep(2)

            pyautogui.moveTo(139, 356) # 1-30
            pyautogui.click() # 1-31
            time.sleep(3)
            x+=1
        else:
            time.sleep(2)
            pyautogui.moveTo(1886, 16) # 1-32
            pyautogui.click() # 1-33
            time.sleep(2)
            pyautogui.moveTo(350, 614) # 1-34
            pyautogui.click() # 1-35
            time.sleep(2)
            print("작업이 완료 되었습니다."+str(verify))
            break


start_up()
empty_bin_macro_start()
