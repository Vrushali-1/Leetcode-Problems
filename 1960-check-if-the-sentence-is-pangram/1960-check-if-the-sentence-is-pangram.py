class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set()
        
        for i in range(len(sentence)):
            alphabets.add(sentence[i])
        
        return True if len(alphabets) == 26 else False
        