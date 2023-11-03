class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def dp(i):
        #     if i in memo:
        #         return memo[i]
            
        #     answer = 1

        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             answer = max(answer,dp(j) + 1)
        #     memo[i] = answer
        #     return memo[i]
        # memo = {}
        # return max(dp(i) for i in range(len(nums)))

        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
           for j in range(i):
               if nums[i] > nums[j]:
                   dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)
