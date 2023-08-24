class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rem, memo):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if memo[rem] != -2:
                return memo[rem]
            
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin, memo)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            
            memo[rem] = min_cost if min_cost != float('inf') else -1
            return memo[rem]
        
        memo = [-2] * (amount + 1)
        return dfs(amount, memo)