class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        answer = []

        for i in range(len(nums)):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            
            deque.append(i)

            if deque[0] + k == i:
                deque.popleft()
            
            if i >= k - 1:
                answer.append(nums[deque[0]])
        return answer