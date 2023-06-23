class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        s1Characters = [0 for i in range(26)]
        s2Characters = [0 for i in range(26)]

        matchCharacters = 0

        for i in range(len(s1)):
            s1Characters[ord(s1[i]) - ord('a')] += 1
            s2Characters[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1Characters[i] == s2Characters[i]:
                matchCharacters += 1
        
        left = 0
        for right in range(len(s1),len(s2)):
            if matchCharacters == 26: return True

            index = ord(s2[right]) - ord('a')
            s2Characters[index] += 1
            if s1Characters[index] == s2Characters[index]:
                matchCharacters += 1
            elif s2Characters[index] - 1 == s1Characters[index]:
                matchCharacters -= 1
            
            index = ord(s2[left]) - ord('a')
            s2Characters[index] -= 1
            if s1Characters[index] == s2Characters[index]:
                matchCharacters += 1
            elif s2Characters[index] + 1 == s1Characters[index]:
                matchCharacters -= 1
            left += 1
        return matchCharacters == 26
