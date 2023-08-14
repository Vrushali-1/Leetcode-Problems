class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = answer = 0
        for right in range(len(nums)):
            if nums[right] != 1:
                counter = 0
            else:
                counter += 1
            answer = max(answer,counter)
        return answer