class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        answer = left = 0
        right = 0
        total = sum(nums)
        for i in range(len(nums)-1):
            left += nums[i]
            right = total - left
            if left >= right:
                answer += 1
        return answer