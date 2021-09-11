"""
#1 변수 선언하여 입력되는 값을 받음
#2 받은 값을 반복하여 age 변수에 다시 넣고 person클래스를 호출하여 age변수를 매개변수로 전달하여 연산을 시작함
#3 전달된 값을 식별하여 결과를 도출할 수 있도록 함

initialAge 13살 보다 작으면 young을 출력하라
initialAge 13살 보다 많거나 같거나 18보다 작으면 teenager를 출력하라
18살 보다 많거나 같으면 old를 출력한다. 
t변수에 입력되는 정수의 값을 넣어준다.
반복적으로 0부터 t의 숫자까지 반복한다.

t = int(input()) #1
for i in range(0, t): #2
    age = int(input()) #2        
    p = Person(age) #2 
    p.amIOld() #3
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")"""



class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        # self: refer self
        self.age=0
        if age<0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console

        if age<13:
            print("You are young.")
        elif age>=13 and age<18:
            print("You are a teenager.")
        elif age>= 18:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age+=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
