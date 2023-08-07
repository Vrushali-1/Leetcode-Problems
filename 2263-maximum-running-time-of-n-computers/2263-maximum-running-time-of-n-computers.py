class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n

        while left < right:
            #mid = (left + right + 1) // 2
            mid = right - (right - left) // 2

            totalPower = 0
            for power in batteries:
                totalPower += min(power,mid)

            if totalPower >= mid * n:
                left = mid
            else:
                 right = mid - 1
        return left

