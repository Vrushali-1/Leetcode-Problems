class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        answer = [-1] * n
        windowSum = 0

        if  k == 0:
            return nums
        
        if 2 * k + 1 > n:
            return answer

        for i in range(2 * k + 1):
            windowSum += nums[i]
        answer[k] = windowSum//(2*k+1)
        for i in range(2*k+1,len(nums)):
            windowSum = windowSum - nums[i-(2*k+1)]  + nums[i]
            answer[i-k] = windowSum//(2*k+1)
        return answer

        

