"""
Question
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
2번째로 큰수 찾기

Natural language

두번째 큰수를 찾는 방법

전체 수를 확인하여 비교 한다 비교하여 가장큰 수를 찾는다 그리고 가장 큰 수 보다 두번째로 작은 수를 식별하여 출력한다.
ex)
배열의 순번
n=5 
2,3,6,6,5
이미 각각 배열에 담겨 있는 수를 알게 되면 두번째 큰수를 식별이 가능해 진다. 컴퓨터 입장에서 각각 arr의 값의 크고 작음이 인식되지 않음을 이해해야 한다. 
arr[0]=?
arr[1]=?
arr[2]=?
arr[3]=?
arr[4]=?

n의 값만큼 아래 내용을 반복해야 한다. 
arr[0]을 compare라는 변수에 넣는다.
arr[0]을 arr[1]째 순번의 값과 비교한다 큰수를 compare라는 변수에 넣는다. 
arr[1]을 arr[2]째 순번의 값과 비교한다 큰수를 compare라는 변수에 넣는다.
arr[2]을 arr[3]째 순번의 값과 비교한다 큰수를 compare라는 변수에 넣는다.
arr[3]을 arr[4]째 순번의 값과 비교한다 큰수를 compare라는 변수에 넣는다.

가장큰 값을 -1한 값을 secondBig 함수에 넣는다
secondBig 값과 arr[0] 비교한다 큰수를 compare라는 변수에 넣는다. 
secondBig 값과 arr[1] 비교한다 큰수를 compare라는 변수에 넣는다. 
secondBig 값과 arr[2] 비교한다 큰수를 compare라는 변수에 넣는다. 
secondBig 값과 arr[3] 비교한다 큰수를 compare라는 변수에 넣는다. 
secondBig 값과 arr[4] 비교한다 큰수를 compare라는 변수에 넣는다. 

secondBig 값과 만약 같은 값을 찾을 경우 secondBig 값을 출력하고 연산을 종료한다. 


Pseudo code

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    compare = arr
    secondBig = 0

    for x in range(n):
      if compare < arr[x]:
        compare = arr[x]

    """print(compare)"""

    for y in range(n):
      secondBig = compare-1
      for z in range(n):
        if secondBig == arr[z]:
          secondBig = arr[z]

    print(secondBig)
