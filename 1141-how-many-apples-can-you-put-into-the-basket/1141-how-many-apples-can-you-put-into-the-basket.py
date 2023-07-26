class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        total, i= 0, 0
        weight.sort()
        
        while i < len(weight) and weight[i] + total <= 5000:
            total += weight[i]
            i += 1
        return i
        