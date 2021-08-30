"""
Natual language
Leap year 찾는 기능 구현
leaf year는 4로 나눌 수 있어야만 하고 혹은 100으로도 나눌 수 있거나 400으로도 나누어 져야 한다.  

Pseudo code
year %4 필수 그리고 year%100 !=0 거나 year%400 == 0

"""


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and (year%100!=0 or year%400==0):
        leap = True
    else:
        leap
    
    return leap

year = int(input())
print(is_leap(year))
