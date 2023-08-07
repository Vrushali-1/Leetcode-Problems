class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(index,path):
            if len(path) == len(digits):
                answer.append("".join(path))
                return
            letters = mappings[digits[index]]
            
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        if not len(digits):
            return []
        
        mappings = { "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz" }
        answer = []
        backtrack(0,[])
        return answer
        