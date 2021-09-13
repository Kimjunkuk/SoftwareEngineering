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
2st
a = '1234'
print a[::2] >> 1 3

a = '1234'
print a[3:0:-1] >> 432

s = "123456"
print(s[1::2])

s = "123456"
print(s[::2])


refer the guidance below from https://stackoverflow.com/questions/9027862/what-does-listxy-do
L[x::y] means a slice of L where the x is the index to start from and y is the step size. Here are some examples you can try in the interpreter

>>> L=range(20)
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
If you want every 3rd element

>>> L[::3]
[0, 3, 6, 9, 12, 15, 18]
Now every third element starting from L[1]

>>> L[1::3]
[1, 4, 7, 10, 13, 16, 19]
Now every third element starting from L[2]

>>> L[2::3]
[2, 5, 8, 11, 14, 17]
You can specify a negative step to go backwards

>>> L[::-1]
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
You can also assign to this slice, but the value must have the same length as the slice you are replacing

>>> L[::3]=[0,0,0,0,0,0,0]
>>> L
[0, 1, 2, 0, 4, 5, 0, 7, 8, 0, 10, 11, 0, 13, 14, 0, 16, 17, 0, 19]
Finally, you can delete every 3rd element like this

>>> del L[::3]
>>> L
[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])


    
    
