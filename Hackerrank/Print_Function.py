"""
Natural language
입력되는 값만큼 줄바꿈 없이 출력하는 기능을 수행하라
반복적으로 입력값만큼 수를 출력하는 기능을 구현

Pseudo code
for i in range (n) i+i end=''

"""


if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i+1, end='')
       
       
