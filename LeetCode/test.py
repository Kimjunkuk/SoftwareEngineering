arr =[3,4,5,1]

left_index=0
center_index=0
right_index=1
n=len(arr) - 1
for x in range(n):
    if arr[center_index] < arr[right_index+x]:
        # print(right_index+x)
        center_index = right_index+x
    elif arr[center_index] > arr[left_index]:
        print(center_index)
    else:
        print(center_index)