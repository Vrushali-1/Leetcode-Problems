class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sequence = 0
        counts = collections.Counter(nums)
        answer = 0 

        
        for num in nums:
            if num - 1 not in counts:
                temp = num
                sequence = 1
                while temp + 1 in counts:
                    sequence += 1
                    temp = temp + 1
                answer = max(answer,sequence)
        return answer
