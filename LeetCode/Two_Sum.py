"""

array배열 중에서 두개의 수를 더한 값이 target의 값이 되는 배열의 번호를 출력하는 문제
어떻게 배열의 두수의 합이 target의 값을 가지는 배열의 순번을 찾을 것 인가? 
0과 1의 합 1과 2의 합 2와 3의 합 비교 

if 

array에 있는 값중 2개의 값이 target으로 주어지는 값이랑 일치하는 값의 자리수를 반환하는 문제

매개변수 : nums 에 List[]값들이 배열로 배치됨 , target 번호 입력됨 
#4.첫번째(nums[0])의 값과 두번째(nums[1])값을 합하여 target값과 비교하는것으로 시작한다. 
#3.반복하여 nums[0]의 자리 부터 +1씩 자리수가 len(nums)까지 증가하도록 한다. 
#2.반복하여 nums[1]의 자리 부터 +1씩 자리수가 증가하도록 한다. 
#4.if nums[j]+nums[i]=target 이 성립한다면 nums[j], nums[i]를 출력하라.  



"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #1
            for j in range(i+1,len(nums)): #2
                if nums[i]+nums[j] == target: #3
                    return i, j #4
        
        
