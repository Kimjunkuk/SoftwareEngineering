"""
1.Logs
두번째로 가장 작은 수를 찾는 문제 

1.하나의 전역 리스트를 생성
2.입력되는 숫자만큼 3,4번 내용을 반복함
3.이름 변수에 삽입되는 이름을 저장함 
4.점수 변수에 삽입되는 점수를 저장함

5.반복적으로 삽입되는 이름 값을 생성한 리스트에 순차적으로 저장함. 
6.반복적으로 삽입되는 점수 값을 생성한 리스트에 순차적으로 저장함. 
7.5번과 6번 과제를 Nested list 기능인 append([변수, 변수])를 활용하여 수행함

8.오름 차순으로 낮은 값부터 가장 높은 값 순으로 데이터 정렬
9.[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]] 형식으로 정렬된 데이터 에서  
10. from operator import itemgetter
11. arr.sort(key=itemgetter(1)) >> 두번째 인덱스를 기준으로 정렬 
13. 배열의 가장 첫번째 arr[0, (key=itemgetter(1))] 수보다 큰 수를 비교하며 찾음 

>>> a = [10, 20, 30]
>>> a.append([500, 600])
>>> a
[10, 20, 30, [500, 600]]
>>> len(a)
4
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    print(arr[1][1]) >>> 37.21
    print(arr[1][1])
    
    rank.sort(key=itemgetter(0))
    print(rank)
            
    arr[x][1] == arr[1][1] and
    
    
2. Natural Language
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#13
#14
#15
#16
#17
#18
"""

from operator import itemgetter

if __name__ == '__main__':
    
    arr=[] #1
    rank=[] #2
    second=0 #3
    
    for _ in range(int(input())): #4
        name = input() #5
        score = float(input()) #6
        arr.append([name, float(score)]) #7
        
    arr.sort(key=itemgetter(1)) #8

    for x in range(len(arr)): #9
        if arr[0][1]!=arr[x][1]: #10
            second = arr[x][1] #11
            break #12
            
    for y in range(len(arr)): #13
        if second==arr[y][1]:  #14
            rank.append(arr[y][0]) #15
            
    rank.sort() #16
    for z in range(len(rank)): #17
        print(rank[z]) #18
    
          
