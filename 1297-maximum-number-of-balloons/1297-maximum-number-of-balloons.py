class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = collections.Counter()
        
        for i in text:
            counter[i] += 1
        
        counter['l'] //= 2
        counter['o'] //=2
        
        answer = min(counter['b'],min(counter['a'],min(counter['l'],min(counter['o'],counter['n']))))
        
        return answer
        