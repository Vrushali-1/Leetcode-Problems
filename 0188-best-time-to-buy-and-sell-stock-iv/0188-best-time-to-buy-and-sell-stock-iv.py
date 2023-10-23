class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def dp(day,holding,remain):
            if day == len(prices) or remain == 0:
                return 0
            
            if (day,holding,remain) in memo:
                return memo[(day,holding,remain)]

            ans = dp(day+1,holding,remain)
            if holding:
                ans = max(ans,prices[day] + dp(day+1,False,remain - 1))

            else:
                ans = max(ans,-prices[day] + dp(day+1,True,remain))
            
            memo[(day,holding,remain)] = ans
            return ans
        
        memo = {}
        return dp(0,False,k)

        