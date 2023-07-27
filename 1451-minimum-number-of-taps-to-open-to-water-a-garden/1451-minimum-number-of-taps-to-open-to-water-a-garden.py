class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxReach = [0 for _ in range(n + 1)]

        for i in range(n+1):
            start = max(0,i - ranges[i])
            end = min(n, i + ranges[i])
            maxReach[start] = max(maxReach[start], end)

        currentPosition, taps, nextPosition = 0, 0, 0

        for i in range(0,n+1):
            if nextPosition < i:
                return -1
            if currentPosition < i:
                taps += 1
                currentPosition = nextPosition
            nextPosition = max(nextPosition, maxReach[i])
        return taps


