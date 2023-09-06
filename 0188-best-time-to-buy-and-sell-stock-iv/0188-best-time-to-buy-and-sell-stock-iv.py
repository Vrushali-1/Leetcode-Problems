class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # @cache
        # def dp(day,holding,remain):
        #     if day == len(prices) or remain == 0:
        #         return 0
            
        #     ans = dp(day+1,holding,remain)
        #     if holding:
        #         ans = max(ans,prices[day] + dp(day+1,False,remain - 1))

        #     else:
        #         ans = max(ans,-prices[day] + dp(day+1,True,remain))
            
        #     return ans
        
        # #memo = {}
        # return dp(0,False,k)
        memo = {}  # Create a memoization dictionary to store computed results.

        def dp(day, holding, remain):
            # Check if the result for this state is already memoized.
            if (day, holding, remain) in memo:
                return memo[(day, holding, remain)]

            if day == len(prices) or remain == 0:
                return 0

            ans = dp(day + 1, holding, remain)
            if holding:
                ans = max(ans, prices[day] + dp(day + 1, False, remain - 1))
            else:
                ans = max(ans, -prices[day] + dp(day + 1, True, remain))

            # Memoize the result for this state.
            memo[(day, holding, remain)] = ans

            return ans

        return dp(0, False, k)

        