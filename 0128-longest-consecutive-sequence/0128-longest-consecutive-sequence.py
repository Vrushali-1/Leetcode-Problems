class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in counts:
                sequence = 1
                temp = num
                while temp + 1 in counts:
                    sequence += 1
                    temp += 1
                answer = max(answer,sequence)
        return answer
            
