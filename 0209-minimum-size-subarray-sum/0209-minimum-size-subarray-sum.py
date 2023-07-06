class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = float('inf')
        current = 0
        for right in range(len(nums)):
            current += nums[right]
            while current >= target:
                current -= nums[left]
                result = min(result,right - left + 1)
                left += 1
        return result if result != float('inf') else 0