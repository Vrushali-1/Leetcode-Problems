class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0

        jump = 0

        while r < (len(nums) - 1):
            maxJump = 0

            for i in range(l,r+1):
                maxJump = max(maxJump,i+nums[i])
            l = r + 1
            r = maxJump
            jump += 1
        return jump