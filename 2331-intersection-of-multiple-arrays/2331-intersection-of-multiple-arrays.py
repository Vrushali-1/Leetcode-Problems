class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numbers = collections.Counter()
        answer = []
        for arr in nums:
            for num in arr:
                numbers[num] += 1
        
        for i in numbers:
            if numbers[i] == len(nums):
                answer.append(i)
        return sorted(answer)