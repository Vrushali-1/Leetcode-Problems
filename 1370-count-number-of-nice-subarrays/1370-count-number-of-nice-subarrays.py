class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        answer = current = 0
        counts[0] = 1

        for i in range(len(nums)):
            current += nums[i] % 2
            answer += counts[current - k]
            counts[current] += 1
        return answer