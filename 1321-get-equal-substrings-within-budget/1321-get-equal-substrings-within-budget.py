class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maximumLength = 0
        maximumCost = 0
        left = 0
        
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            maximumCost += cost

            while maximumCost > maxCost:
                cost = abs(ord(s[left]) - ord(t[left]))
                maximumCost -= cost
                left += 1
            maximumLength = max(maximumLength,right - left + 1)

        return maximumLength
