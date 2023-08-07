class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        if n == 1:
            return [i for i in range(0,10)]
        def dfs(currentNum,N):
            if N == 0:
                answer.append(currentNum)
                return
            
            tail = currentNum % 10
            digits = set([tail + k, tail - k])

            for digit in digits:
                if  0 <= digit < 10:
                    newNum = currentNum * 10 + digit
                    dfs(newNum, N-1)
        
        answer = []
        for num in range(1,10):
            dfs(num,n-1)
        return answer