class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0, 0
        answer = 0

        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j+= 1
        
        return 0 if j == len(t) else len(t) - j