class NumArray:

    numbers = list()
    def __init__(self, nums: List[int]):
        n  = len(nums)
        self.numbers = [0 for i in range(n + 1)]
        for i in range(len(nums)):
            self.numbers[i + 1] = self.numbers[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.numbers[right+1] - self.numbers[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)