class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        def dp(i,remain):
            if i == len(piles) or remain == 0:
                return 0
            
            if (i,remain) in memo:
                return memo[(i,remain)]
            
            answer = dp(i+1,remain) #skip the pile
            current = 0
            for j in range(min(remain,len(piles[i]))):
                current += piles[i][j]
                answer = max(answer,current + dp(i+1,remain-j-1))
            
            memo[(i,remain)] = answer

            return answer
        
        memo = {}
        return dp(0,k)