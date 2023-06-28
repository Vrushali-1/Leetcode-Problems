class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        answer = current = 0

        for i in range(len(nums)):
            current += nums[i]
            answer += prefix[current - k]
            prefix[current] += 1

        return answer