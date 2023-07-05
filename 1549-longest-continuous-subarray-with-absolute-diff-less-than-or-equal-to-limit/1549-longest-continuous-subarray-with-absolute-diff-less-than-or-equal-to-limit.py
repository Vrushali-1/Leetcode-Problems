class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = collections.deque()
        decreasing = collections.deque()

        left = answer = 0

        for right in range(len(nums)):

            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])


            while decreasing[0] - increasing[0] > limit:
                if increasing[0] == nums[left]:
                    increasing.popleft()
                if decreasing[0] == nums[left]:
                    decreasing.popleft()
                left += 1
            
            answer = max(answer,right - left + 1)

        return answer
                
        