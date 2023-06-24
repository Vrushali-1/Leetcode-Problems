class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0
        for left in range(len(nums)):
            if nums[left] != 0 and nums[right] == 0:
                nums[right], nums[left] = nums[left], nums[right]

            # wait while we find a non-zero element to
            # swap with you
            if nums[right] != 0:
                right += 1