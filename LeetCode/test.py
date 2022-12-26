min_index=1
center_index=0
max_index=n
for x in range(n):
    center_index=(max_index + min_index)//2
    if guess(center_index) == -1:
        max_index = center_index
    if guess(center_index) == 1:
        min_index = center_index
    if guess(center_index) == 0:
        return center_index 
        break
