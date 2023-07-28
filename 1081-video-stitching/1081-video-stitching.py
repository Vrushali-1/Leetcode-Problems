class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(reverse = True)
        
        count = 0
        current = 0

        while current < time:
            heap = []
            while clips and clips[-1][0] <= current:
                heapq.heappush(heap, -clips.pop()[1])
            if not heap:
                return -1
            current = -heapq.heappop(heap)
            count += 1
        return count