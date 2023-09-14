class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, free = -prices[0], 0

        for i in range(1,len(prices)):
            temp = hold
            hold = max(hold,free - prices[i])
            free = max(free, temp + prices[i] - fee) 
        
        return free
        