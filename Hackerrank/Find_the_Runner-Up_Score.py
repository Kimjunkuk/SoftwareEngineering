"""
Question
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
2번째로 큰수 찾기

Natural language
1nd
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
__________________________________________________________________________________________________________________________
2nd
arr를 내림 차순 정렬

arr[0]-1의 값과 나머지 값을 비교 하여 동일한 값 식별 및 출력 작업을 -1연산을 반복하며 진행
__________________________________________________________________________________________________________________________
3nd
**2nd 문제점 음수값의 배열과 큰 갭의 배열의 값의 두번째 큰수를 식별하는 알고리즘에 한계가 있었음
**python list 의 함수 사용할것

arr를 내림 차순 정렬
첫번째 값을 비교함수에 저장
반복적으로 비교함수의 값과 작은 값을 식별 하도록 하되 작은 값을 식별시 바로 반복문 종료하도록 설계
결과 출력

Pseudo code

arr.sort(reverse=True)
compare에  arr[0] 저장
반복문 실행
조건compare > int(arr[x]) 성립시 result변수에 int(arr[x]) 저장 후 반복문 


"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = 0

    arr.sort(reverse = True) 
    
    compare = int(arr[0])
    
    
    for x in range(n):
        if compare > int(arr[x]):
            result = int(arr[x])
            break

    print(result)

