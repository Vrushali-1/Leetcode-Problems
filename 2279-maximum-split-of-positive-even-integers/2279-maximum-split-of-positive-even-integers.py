class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        
        result = []
        current = 2
        while current <= finalSum:
            if finalSum - current == 0 or finalSum - current > current:
                result.append(current)
                finalSum -= current
                current += 2
            else:
                current = finalSum
        return result