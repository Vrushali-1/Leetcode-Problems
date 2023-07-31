class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            result = 0

            for num in nums:
                result += ceil(num / divisor)
            return result <= threshold 
        
        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                #answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return left