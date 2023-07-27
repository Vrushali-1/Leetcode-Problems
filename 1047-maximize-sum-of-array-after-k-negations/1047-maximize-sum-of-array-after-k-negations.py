class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k != 0:
            heapq.heappush(nums,-heapq.heappop(nums))
            k -= 1
        return sum(nums)