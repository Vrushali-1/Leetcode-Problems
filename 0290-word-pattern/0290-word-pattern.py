class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        wordsMapping = {}
        letterMapping = {}

        
        for word, letter in zip(words,pattern):
            if word not in wordsMapping and letter not in letterMapping:
                wordsMapping[word] = letter
                letterMapping[letter] = word
            elif wordsMapping.get(word) != letter or letterMapping.get(letter) != word:
                return False
        return len(words) == len(pattern)