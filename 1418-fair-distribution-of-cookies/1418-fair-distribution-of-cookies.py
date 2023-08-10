class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        curr = [0 for _ in range(k)]
        n = len(cookies) 
        def backtrack(i,zero_count):
            if n - i < zero_count:
                return float('inf')
            
            if i == n:
                return max(curr)
            
            answer = float('inf')
            for j in range(k):
                zero_count -= int(curr[j]==0)
                curr[j] += cookies[i]
                answer = min(answer,backtrack(i+1,zero_count))
                curr[j] -= cookies[i]
                zero_count += int(curr[j]==0)
            return answer
        
        return backtrack(0,k)

        # cur = [0] * k
        # n = len(cookies)

        # def dfs(i, zero_count):
        #     # If there are not enough cookies remaining, return `float('inf')` 
        #     # as it leads to an invalid distribution.
        #     if n - i < zero_count:
        #         return float('inf')
            
        #     # After distributing all cookies, return the unfairness of this
        #     # distribution.
        #     if i == n:
        #         return max(cur)
            
        #     # Try to distribute the i-th cookie to each child, and update answer
        #     # as the minimum unfairness in these distributions.
        #     answer = float('inf')
        #     for j in range(k):
        #         zero_count -= int(cur[j] == 0)
        #         cur[j] += cookies[i]
                
        #         # Recursively distribute the next cookie.
        #         answer = min(answer, dfs(i + 1, zero_count))
                
        #         cur[j] -= cookies[i]
        #         zero_count += int(cur[j] == 0)
            
        #     return answer
        
        # return dfs(0, k)