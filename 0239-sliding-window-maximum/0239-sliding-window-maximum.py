class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = collections.deque() #deque to maintain maximum number
        left = 0
        answer = []

        for right in range(k): #loop to fill elements untill size becomes k i.e first window
            while maximum and maximum[-1] < nums[right]:
                maximum.pop()
            maximum.append(nums[right])

        answer.append(maximum[0])

        for right in range(k,len(nums)): #for rest of the windows
            while maximum and maximum[-1] < nums[right]:
                maximum.pop()
            maximum.append(nums[right])
            if maximum[0] == nums[left]:
                maximum.popleft()
            left += 1
            answer.append(maximum[0])

        return answer
