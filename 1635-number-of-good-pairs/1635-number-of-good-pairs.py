class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = collections.Counter()
        answer = 0
        for num in nums:
            if num in counts:
                answer += counts[num]
            counts[num] += 1
        return answer
