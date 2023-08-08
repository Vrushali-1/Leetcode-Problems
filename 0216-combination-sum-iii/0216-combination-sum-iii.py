class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remaining, combination, start):
            if remaining == 0 and len(combination) == k:
                answer.append(combination[:])
                return
            
            if remaining < 0 or len(combination) == k:
                return
            
            for digit in range(start,10):
                combination.append(digit)
                backtrack(remaining - digit, combination, digit + 1 )
                combination.pop()
        
        answer = []
        backtrack(n,[],1)
        return answer
