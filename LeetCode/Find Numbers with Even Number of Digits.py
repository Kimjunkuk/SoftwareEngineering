class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # [12, 345, 2, 6, 7896]
        # map->["12", "345", "2", "6", "7896"]
        # map->[2, 3, 1, 1, 4]
        # filter->[2, 4]
        # reduce->2

        res=0
        for num in nums:
            if (len(str(num)))%2 == 0:
                res+=1
        return res