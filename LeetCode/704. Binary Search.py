# Study
def search(arr, target):
  row_index = 0
  mid_index = 0
  high_index = len(arr)-1

  while high_index >= row_index:
    mid_index = (high_index+row_index)//2

    if target > arr[mid_index]:
      row_index = mid_index+1
    elif target < arr[mid_index]:
      high_index = mid_index-1
    else:
      return mid_index
  return -1


arr = [1, 2, 3, 4, 5, 6, 7]
target = 7

final_result = search(arr, target)

print("The final result:["+str(final_result)+"]")

# result
# Runtime: 438 ms, faster than 13.98% of Python3 online submissions for Binary Search.
# Memory Usage: 15.6 MB, less than 24.85% of Python3 online submissions for Binary Search.

# test
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        row_index = 0
        mid_index = 0
        high_index = len(nums)-1

        while high_index >= row_index:
            mid_index = (high_index+row_index)//2
            if target > nums[mid_index]:
                row_index = mid_index+1
            elif target < nums[mid_index]:
                high_index = mid_index-1
            else:
                return mid_index

        return -1

