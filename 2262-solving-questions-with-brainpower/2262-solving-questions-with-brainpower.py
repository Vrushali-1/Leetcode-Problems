class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i):
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i]

            j = i + questions[i][1] + 1
            memo[i] = max(questions[i][0]+dp(j), dp(i+1))
            return memo[i]
        memo = {}
        return dp(0)