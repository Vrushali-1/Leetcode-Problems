class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = collections.Counter(magazine)
        
        for i in range(len(ransomNote)):
            if counts[ransomNote[i]] <= 0:
                return False
            
            counts[ransomNote[i]] -= 1
        return True