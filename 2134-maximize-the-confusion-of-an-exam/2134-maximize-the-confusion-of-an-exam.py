class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, answer, maximum = 0, 0, 0
        
        counts = collections.Counter()

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            if counts[answerKey[right]] > maximum:
                maximum = counts[answerKey[right]]

            windowLength = right - left + 1
            
            if windowLength - maximum > k:
                counts[answerKey[left]] -= 1
                left += 1
                
            answer = max(answer, right - left + 1)
        return answer

