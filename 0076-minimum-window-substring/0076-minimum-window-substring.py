class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        target = collections.Counter(t)
        unique = len(target)
        inputString = collections.Counter()
        matchCounter = 0

        finalLeft = 0
        finalRight = 0
        finalLength = float('inf')

        left = 0
        for right in range(len(s)):
            inputString[s[right]] += 1

            if(inputString[s[right]] == target[s[right]]):
                matchCounter += 1
            
            while (matchCounter == unique):
                if right - left + 1 < finalLength:
                    print('inside less length',right - left + 1)
                    finalLength = right - left + 1
                    finalLeft = left
                    finalRight = right
                if inputString[s[left]] == target[s[left]]: matchCounter -= 1
                inputString[s[left]] -= 1
                left += 1
        return s[finalLeft:finalRight+1] if finalLength != float('inf') else ""
