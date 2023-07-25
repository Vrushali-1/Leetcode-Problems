class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        elements = [0 for _ in range(n)]
        minheap = [[sequence[0],index] for index,sequence in enumerate(nums)]
        answer = []

        #currentMin = min(pair[0] for pair in minheap)
        currentMax = max(pair[0] for pair in minheap)
        heapq.heapify(minheap)
        currentMin = minheap[0][0]
        
        answer = [currentMin,currentMax]

        if currentMin == currentMax:
            return answer
        
        heapq.heapify(minheap)

        while True:
            _,index = heapq.heappop(minheap)

            elements[index] += 1

            if elements[index] == len(nums[index]):
                return answer
            
            if nums[index][elements[index]] > currentMax:
                currentMax = nums[index][elements[index]]

            heapq.heappush(minheap, [nums[index][elements[index]],index])
            currentMin = minheap[0][0]

            if currentMax - currentMin < answer[1] - answer[0]:
                answer = [currentMin,currentMax]

            if currentMin == currentMax:
                return answer
