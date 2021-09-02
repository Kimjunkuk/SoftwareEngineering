"""

하나의 리스트를 생성해 학생이름과 점수가 하나의 값으로 리스트에 저장 될 수 있도록 함. 

구현된 내용
삽입되는 input의 숫자만큼 아래 내용을 반복함
insert the input values to the name variable 
insert the input values to the score variable
**Local 로컬 변수로 선언되었음
**Grobal 저장매체 필요할 것으로 판단됨 
**이중 for문의 원리를 사용
반복적으로 삽입되는 이름 값을 생성한 리스트에 순차적으로 저장함. 
반복적으로 삽입되는 점수 값을 생성한 리스트에 순차적으로 저장함. 
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
