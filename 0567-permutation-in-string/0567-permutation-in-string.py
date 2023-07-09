class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = [0 for i in range(26)]
        s2Count = [0 for i in range(26)]

        matchCount = left = 0

        if len(s1) > len(s2) or not s2:
            return False
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matchCount += 1
        
        if matchCount == 26:
            return True

        for right in range(len(s1),len(s2)):
            if matchCount == 26:
                return True

            index = ord(s2[right]) - ord('a') #index of new right ele
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matchCount += 1
            elif s2Count[index] - 1 == s1Count[index]:
                matchCount -= 1
            
            index = ord(s2[left]) - ord('a') #index of the ele to be removed
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matchCount += 1
            elif s2Count[index] + 1 == s1Count[index]:
                matchCount -= 1

            left += 1 #increment left

        return matchCount == 26

        