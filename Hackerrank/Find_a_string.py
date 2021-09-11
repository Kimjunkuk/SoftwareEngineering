"""
1st
def count_substring(string, sub_string):
    num=0
    print("len_substring:"+str(len(sub_string)))
    for x in range(len(string)):
      y=int(len(sub_string))
      print("x:"+str(x))
      print("y"+str(y))
      if sub_string != string[x:y]:
        print("range"+str(x)+":"+str(y)+":"+string[x:y])
        y+=1
      else:
        num+=1
    print(num)
    return num

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
    
    #1 함수에 string 매개변수와 sub_string 매개변수를 입력 
    #2 num 변수를 0으로 초기화
    #3 y변수에 입력된 매개변수 sub_string의 길이를 저장함
    #4 z변수를 0으로 초기화
    #5 x=0부터 string의 길이만큼 6번 작업부터 반복함 >>만약 string = "ABCDCDC"라면 0부터 6까지 반복
    [0:2]=ABC, [1:3]=BCD, [2:4]=CDC, [3:5]=DCD, [4:6]=CDC
    반복문은 0:2의 값부터 각각 1씩증가하면서 위치를 조건문으로 확인시켜 주면된다.
    #6 만약 sub_string=CDC 값이string의 [0:2]=ABC값과 같지 않다면 z와 y를 1씩 증가시켜라

    
"""


def count_substring(string, sub_string): #1
    num=0 #2
    z=0 #4
    y=len(sub_string)
    for x in range(len(string)): #5
        if str(sub_string) == str(string[int(z):int(y)]): #6
            num+=1 
        z+=1
        y+=1 
    return num #

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
