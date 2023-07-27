class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        while k != 0:
            nums.sort()
            nums[0] = -nums[0]
            total = sum(nums)
            k -= 1
        return total