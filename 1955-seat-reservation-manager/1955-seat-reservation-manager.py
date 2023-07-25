class SeatManager:

    def __init__(self, n: int):
        self.minheap = list([i for i in range(1,n+1)])
        heapq.heapify(self.minheap)
        

    def reserve(self) -> int:
        return heapq.heappop(self.minheap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minheap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)