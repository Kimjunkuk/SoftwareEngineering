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


#condition
# 1. sorted array
# 2. you will be find the target value by middle value if you arroch with a binary search algorithm 

# question list
# 1. Can use the math libary? math.trunc(x) << round down


# natural language
# binary search approch
# declare low_value variable for a lowest value
# declare mid_value variable for a middle value
# declare high_value variable for a hightest value
# declare target variable (x) for taget 
# declare middle value variable (y) for mid_value 
# -find the middle value and compare with a target value if the target value is smaller than middle value keep search left side 
# or if the taget value is bigger than middle value keep search right side. 
when I get a  middle index number then get value with the middle index number if it is smaller than target value please research left side values
if middle value smaller than target value next? 
find the middle value index first by array first index and previous index number. because the previous number going to be lastest value's index. 
so middle value's index should come from the first valuse's index and lastest value's index. 
middle value index can get by first value index and last value index 
last[y]/2 last value index devide by 2 if it float we can use math.trunc round down function. 
last[-1]/2


# code
import math

def search(arr, target):
  
  x=taget
  y=0 # mid value
  y=math.trunc(len(arr)/2)
  

arr=[1,2,3,5,5,6]
target=9

search(arr, target)
