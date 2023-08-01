class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArray = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            subArray = max(subArray,currentSum)
        return subArray