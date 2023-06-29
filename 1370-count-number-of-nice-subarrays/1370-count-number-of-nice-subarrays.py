class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        current = answer = 0

        for num in nums:
            current+= num%2
            answer += count[current-k]
            count[current] += 1
        return answer 