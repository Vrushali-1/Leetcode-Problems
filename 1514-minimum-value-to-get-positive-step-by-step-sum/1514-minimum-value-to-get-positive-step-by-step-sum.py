class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        addition = 0
        minimum = 0
        for i in range(len(nums)):
            addition += nums[i]
            print(addition)
            minimum = min(minimum,addition)
        return abs(minimum) + 1

        