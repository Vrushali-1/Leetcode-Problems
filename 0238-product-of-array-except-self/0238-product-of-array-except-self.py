class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for i in range(len(nums))]
        n = len(nums)

        for i in range(1,n):
            answer[i] = nums[i-1] * answer[i-1]
        
        rightproduct = 1

        for i in range(n-1,-1,-1):
            answer[i] = rightproduct * answer[i]
            rightproduct *= nums[i]
        
        return answer
            