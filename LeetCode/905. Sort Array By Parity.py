arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
n = len(arr)

for i in range(0, n-1): #1
    least = i
    for j in range (i+1, n):
        if arr[least] > arr[j]:
            least = j
    arr[i], arr[least] = arr[least], arr[i]
    
print(arr)


#1. 0부터 n-1==8 array 길이의 -1 의 값만큼 반복 수행 << 총 인덱스만큼만 반복 필요 
#2. least=i 선언
#3. 이중 반복문에서 상위반복문 의 +1 만큼 진행 