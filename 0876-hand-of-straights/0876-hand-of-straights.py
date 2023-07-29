class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counts = collections.Counter(hand)
        minheap = list(counts.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for i in range(first, first+groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True