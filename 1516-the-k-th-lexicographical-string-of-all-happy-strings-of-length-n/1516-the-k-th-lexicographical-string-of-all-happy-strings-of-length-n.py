class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(current,last):
            if len(current) == n:
                answer.append("".join(current[:]))
                return
            
            for c in ['a','b','c']:
                if c != last:
                    current.append(c)
                    backtrack(current,c)
                    current.pop()
        
        answer = []
        backtrack([],"")

        return answer[k - 1] if len(answer) >= k else ""