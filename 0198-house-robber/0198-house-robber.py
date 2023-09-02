class Solution:
    def rob(self, nums: List[int]) -> int:
        #top-down approach
        # def dp(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0],nums[1])
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(dp(i-2) + nums[i],dp(i-1))
        #     return memo[i]
        # memo = {}
        # return dp(len(nums) - 1)

        #bottom-up approach
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [0 for _ in range(n)]
        # dp[0], dp[1] = nums[0], max(nums[0],nums[1])

        # for i in range(2,n):
        #     dp[i] = max(dp[i-2] + nums[i],dp[i-1])
        # return dp[n-1]

        #bottom-up approach with space optimizaion
        n = len(nums)
        if n == 1:
            return nums[0]
        back_one,back_two = max(nums[0],nums[1]),nums[0]
        for i in range(2,n):
            back_one,back_two = max(back_two+nums[i],back_one),back_one
        return back_one