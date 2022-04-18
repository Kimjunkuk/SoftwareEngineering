import pyautogui
import time
import os
from datetime import datetime
# while True:
#     print("Current Mouse Position: ",pyautogui.position())
#     time.sleep(1)

# from datetime import datetime

# s=datetime.now().strftime('%H:%M:%S')
# print(s)

# print(os.path.join(os.getcwd(), "SBins.xlsx"))

# print("hello"+os.getcwd())


s=datetime.now().strftime('%H')
# print(s)

if int(s) >=11:
    print("hellow")
# if s == '11:05' or s == '15:01':
#     time.sleep(3600)