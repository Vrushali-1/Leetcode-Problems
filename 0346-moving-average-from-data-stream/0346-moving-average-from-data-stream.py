class MovingAverage:
    
    def __init__(self,size:int):
        self.size = size
        self.queue = collections.deque()
        self.windowSum = 0
        self.count = 0
    
    def next(self,val:int) -> float:
        self.count += 1
        self.queue.append(val)
        temp = self.queue.popleft() if self.count > self.size else 0
        self.windowSum = self.windowSum + val - temp
        return self.windowSum/min(self.count,self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)