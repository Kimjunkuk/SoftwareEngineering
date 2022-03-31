# Given an array of integers nums which is sorted in ascending order, 
#and an integer target, write a function to search target in nums. 
#If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# question list
1. Can use the math libary? math.trunc(x) << round down


# natural language
binary search approch
1. declare target variable (x) for taget 
2. declare middle value variable (y) for mid_value 
3. find the middle value 
nums


# code
import math

def search(arr, target):
  x=taget
  y=0 # mid value
  y=math.trunc(len(arr)/2)
  

arr=[1,2,3,5,5,6]
target=9

search(arr, target)
