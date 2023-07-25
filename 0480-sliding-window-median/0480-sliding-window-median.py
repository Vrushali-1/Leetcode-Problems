class Solution:
    def find_median(self, max_heap, min_heap, heap_size):
            if heap_size % 2 == 1:
                return -max_heap[0]
            else:
                return (-max_heap[0] + min_heap[0]) / 2
                
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # answer = []
        # counts = collections.Counter()
        # maxheap = []
        # minheap = []

        # for i in range(k):
        #     heapq.heappush(maxheap,-nums[i])
        
        # for i in range(k//2):
        #     heapq.heappush(minheap, -heapq.heappop(maxheap))
        
        # for i in range(k,len(nums)):
        #     if len(maxheap) > len(minheap):
        #         answer.append(-maxheap[0])
        #     else:
        #         answer.append((-maxheap[0] + minheap[0])/2)
            
        #     balance = 0
        #     outgoing = nums[i-k]
        #     incoming = nums[i]

        #     balance += -1 if outgoing <= -maxheap[0] else 1
        #     counts[outgoing] += 1

        #     if maxheap and incoming <= -maxheap[0]:
        #         heapq.heappush(maxheap, -incoming)
        #         balance += 1
        #     else:
        #         heapq.heappush(minheap,incoming)
        #         balance -= 1

        #     if balance < 0:
        #         heapq.heappush(maxheap, -heapq.heappop(minheap))
        #         balance += 1
        #     if balance > 0:
        #         heapq.heappush(minheap,-heapq.heappop(maxheap))
        #         balance -= 1
            
        #     while minheap[0] in counts:
        #         if counts[minheap[0]] == 1:
        #             del counts[minheap[0]]
        #         else:
        #             counts[minheap[0]] -=1
            
        #     while -maxheap[0] in counts:
        #         if counts[-maxheap[0]] == 1:
        #             del counts[-maxheap[0]]
        #         else:
        #             counts[-maxheap[0]] -=1
        #     print(minheap,maxheap)
        #     #break
        # return answer
        
        
        
        max_heap = []
        min_heap = []
        heap_dict = defaultdict(int)
        result = []
        
        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))
        
        median = self.find_median(max_heap, min_heap, k)
        result.append(median)
        
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1
            
            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])
            
            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)
            
            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)
        
        return result
        


            
