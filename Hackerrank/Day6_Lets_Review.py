# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
1st
n=2
s=Hacker
n의 숫자만큼 string 값을 받아 string을 반반으로 분리하여 출력할 수 있는 프로그램 구성

s변수 선언 input() 함수를통해 스트링값 입력 받음 
입력된 string값의 절반 값을 출력시 공백 추가 후 나머지 절반을 출력한다. 
만약 y의 값이 y%2==0 (짝수) 이거나 y==0 이면 

만약 y의 값이 y%2==1 (홀수) 이면 
y[int((len(s))/2)-1] 절반값

n=int(input())
for x in range(n):
    s=input()
    for y in range(len(s)):
        print(s[y], end="")
        if int((len(s))/2)-1==y:
            print(" ", end="")
    print("")
            
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]

for x in range(n):
    s=input()
    for y in range(len(s)):
        l.insert(y)
        if l

print(l)


    
    
