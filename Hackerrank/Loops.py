"""
Natural language
n의 범위 만큼 반복하면서 i*i를 곱한 값을 각줄에 인쇠하여라
print i*i range n 


Pseudo code
loop range n print i*i
"""


if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i*i)
