class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(remaining):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            if memo[remaining] != -2:
                return memo[remaining]
            min_cost = float('inf')
            for coin in coins:
                result = dp(remaining - coin)
                if result != -1:
                    min_cost = min(min_cost,result + 1)
            memo[remaining] = min_cost if min_cost != float('inf') else -1
            return memo[remaining]
        memo = [-2 for _ in range(amount + 1)]
        return dp(amount)