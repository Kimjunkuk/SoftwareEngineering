

"""
This code seems to be trying to check if a list contains any duplicates. It does this by iterating through the list and comparing each element to every other element, and returning True if it finds any duplicates.
There are a few issues with this approach:
It has a time complexity of O(n^2), which means that it takes longer to run as the size of the list increases. This can be a problem if the list is very large.
It doesn't take advantage of the fact that Python sets only allow unique elements, which means that we can check for duplicates much more efficiently by using a set.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            search_value=nums[x]
            # len길이 만큼 반복하면서 search_value와 compare_value를 비교하여
            for y in range(len(nums)-1):
                if x == y:
                    y+=1 
                compare_value=nums[y]
                # 비교 중 같은 값이 나오면 True 를 반환하고 반복 작업을 중단 하여라
                #index 값이 같다면 비교를 하지 않도록 해야함 
                if search_value==compare_value:
                    return True
                    break	
        return False"""


""" Sadly I uesed set() method...."""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        if len(set(nums)) < len(nums):
            return True