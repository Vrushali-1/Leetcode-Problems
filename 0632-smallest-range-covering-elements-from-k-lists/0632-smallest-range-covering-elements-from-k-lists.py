class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # n = len(nums)
        # element = [0 for _ in range(n)]
        # minheap = [[sequence[0],index] for sequence, index in enumerate(nums)]
        # answer = []

        # currentMin = min(pair[0] for pair in minheap)
        # currentMax = max(pair[0] for pair in minheap)

        # answer = [currentMin,currentMax]

        # if currentMin == currentMax:
        #     return answer
        
        # minheap.heapify()

        n = len(nums)
        curr_idx = [0 for _ in range(n)]
        heap = [[n[0], idx] for idx, n in enumerate(nums)]

        curr_min = min([h[0] for h in heap])
        curr_max = max([h[0] for h in heap])
        res = [curr_min, curr_max]
        if curr_min == curr_max: return res
        # print(curr_min, curr_max)
        heapq.heapify(heap)
        while True:
            _, idx = heapq.heappop(heap)
            curr_idx[idx] += 1
            if curr_idx[idx] == len(nums[idx]):
                return res
            if nums[idx][curr_idx[idx]] > curr_max:
                curr_max = nums[idx][curr_idx[idx]]
            heapq.heappush(heap, [nums[idx][curr_idx[idx]], idx])
            curr_min = heap[0][0]
            
            if curr_max - curr_min < res[1] - res[0]:
                res = [curr_min, curr_max]
            if curr_min == curr_max:
                return res
        

