class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        addition = 0

        for count in counts:
            if counts[count] == 1:
                addition += count
        return addition