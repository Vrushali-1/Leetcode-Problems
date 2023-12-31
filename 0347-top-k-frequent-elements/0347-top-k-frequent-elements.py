class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = collections.Counter(nums)
        # bucket = [[] for i in range(len(nums) + 1)]
        # answer = []

        # for count in counts:
        #     bucket[counts[count]].append(count)
        
        # for i in range(len(bucket) - 1, 0 , -1):
        #     for c in bucket[i]:
        #         if k==0:
        #             break
        #         answer.append(c)
        #         k -= 1
        # return answer

        counts = collections.Counter(nums)
        heap = []

        for key, value in counts.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]