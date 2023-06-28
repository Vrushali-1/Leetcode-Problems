class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     numbers = set(nums)
    #     for i in range(len(nums) + 1):
    #         if i not in numbers:
    #             return i
    
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n+1))//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        