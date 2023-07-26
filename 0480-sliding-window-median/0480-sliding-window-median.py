class Solution:

    def getMedian(self, maxheap, minheap, heapSize):
        if heapSize % 2 == 1:
            return -maxheap[0]
        else:
            return (-maxheap[0] + minheap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        answer = []
        counts = collections.Counter()
        maxheap = []
        minheap = []

        for i in range(k):
            heapq.heappush(maxheap,-nums[i])
        
        for i in range(k//2):
            heapq.heappush(minheap, -heapq.heappop(maxheap))
        
        answer.append(self.getMedian(maxheap,minheap,k))
        
        for i in range(k,len(nums)):
            outgoing = nums[i-k]
            incoming = nums[i]

            balance = -1 if outgoing <= -maxheap[0] else 1
            counts[outgoing] += 1

            if incoming <= -maxheap[0]:
                heapq.heappush(maxheap, -incoming)
                balance += 1
            else:
                heapq.heappush(minheap,incoming)
                balance -= 1

            if balance < 0:
                heapq.heappush(maxheap, -heapq.heappop(minheap))
            elif balance > 0:
                heapq.heappush(minheap,-heapq.heappop(maxheap))
            
            while maxheap and counts[-maxheap[0]] > 0:
                counts[-maxheap[0]] -=1
                heapq.heappop(maxheap)
            
            while minheap and counts[minheap[0]] > 0:
                counts[minheap[0]] -=1
                heapq.heappop(minheap)   

            answer.append(self.getMedian(maxheap,minheap,k))
        return answer
            
            
