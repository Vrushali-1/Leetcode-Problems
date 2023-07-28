class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pair = list(zip(capital,profits))
        pair.sort()
        maxheap = []
        pointer = 0
        n = len(profits)
        
        for i in range(k):
            while pointer < n and pair[pointer][0] <= w:
                heapq.heappush(maxheap, -pair[pointer][1])
                pointer += 1
            if maxheap:
                w += -heapq.heappop(maxheap)
        return w
