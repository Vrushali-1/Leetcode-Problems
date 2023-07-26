def sortSecond(val):
        return val[1]
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=sortSecond, reverse= True)
        answer = 0
        for pair in boxTypes:
            boxCount = min(truckSize,pair[0])
            answer += pair[1] * boxCount
            truckSize -= boxCount
            
            if truckSize == 0:
                break
        return answer