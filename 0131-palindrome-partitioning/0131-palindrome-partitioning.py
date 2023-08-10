class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isValid(low,high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        def backtrack(start,current):
            if start >= len(s):
                answer.append(current[:])
                return
            
            for i in range(start,len(s)):
                if isValid(start,i):
                    current.append(s[start:i+1])
                    backtrack(i+1,current)
                    current.pop()
        
        answer = []
        backtrack(0,[])
        return answer