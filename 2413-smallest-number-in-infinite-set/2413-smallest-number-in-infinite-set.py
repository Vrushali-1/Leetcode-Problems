class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.counts = set()
        self.minheap = []
        

    def popSmallest(self) -> int:
        if self.minheap:
            temp = heapq.heappop(self.minheap)
            self.counts.remove(temp)
            return temp
        else:
            temp = self.smallest
            self.smallest += 1
            return temp
        

    def addBack(self, num: int) -> None:
        if num >= self.smallest or num in self.counts:
            return
        else:
            heapq.heappush(self.minheap,num)
            self.counts.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)