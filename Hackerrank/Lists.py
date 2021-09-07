"""
N은 명령어의 수를 나타낸다
n은 명령어,인덱스 넘버, 값 을 포함한다

주어지는 명령어를 반복적으로 수행한다. 
N값 반복문의 범위를 설정할때 사용
n의 값은 배열에 삽입하여 인덱스의 값에 해당하는 기능을 수행할 수 있도록 구현 

식별용 빈 리스트 한개 생성함
결과물을 담을 리스트 한개 생성함
입력된 3가지 값을 개별값으로 식별할 수 있도록 해야함 >> n.split()함수 사용
ex) insert 0 5 => "insert" ,0 ,5

반복적 명령어 식별 
"insert", "print", "remove", "append", "sort", "pop", "reverse" == 7 commands
if r[x][0](항상 첫번째 값이 명령어 값을 가짐)=="insert"

    for x in range(N):
        l = n.split()
        if l[0]=="insert":
            resault.insert(int(l[1]),int(l[2]))
        elif l[0]=="remove":
            resault.remove(int(l[1]))
        elif l[0]=="append":
            resault.append(int(l[1]))
        elif l[0]=="sort":
            resault.sort()
        elif l[0]=="pop":
            resault.pop()
        elif l[0]=="reverse":
            resault.reverse
        elif l[0]=="print":
            print(resault)



"""

if __name__ == '__main__':
    N = int(input())
