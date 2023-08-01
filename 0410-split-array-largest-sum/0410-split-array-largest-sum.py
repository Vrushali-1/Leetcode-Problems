class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(maxSum):
            currentSum = 0
            splits = 0

            for num in nums:

                if currentSum + num <= maxSum:
                    currentSum += num
                else:
                    splits += 1
                    currentSum = num
            return splits + 1
        

        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if check(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

        