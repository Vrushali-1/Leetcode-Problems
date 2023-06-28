class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        characters = collections.Counter()
        for char in s:
            characters[char] += 1
        
        return len(set(characters.values())) == 1
