"""
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
11. arr.sort(key=itemgetter(2)) >> 두번째 인덱스를 기준으로 정렬 

>>> a = [10, 20, 30]
>>> a.append([500, 600])
>>> a
[10, 20, 30, [500, 600]]
>>> len(a)
4
"""

from operator import itemgetter

if __name__ == '__main__':
    
    arr=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, float(score)])
    
    arr.sort(key=itemgetter(1))
    print(arr)
        
