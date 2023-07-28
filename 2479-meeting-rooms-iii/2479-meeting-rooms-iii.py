class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0 for _ in range(n)]
        available = [i for i in range(n)]
        busy = [] #heap sorted according to end time

        meetings.sort()

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy,(end,room))
            else:
                previousEnd, room = heapq.heappop(busy)
                heapq.heappush(busy,(previousEnd + end - start, room))

            count[room] += 1

        return count.index(max(count)) 