class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(minTime):
            trips = 0
            for t in time:
                trips += minTime// t
            return trips >= totalTrips
        
        left,right = 1, max(time) * totalTrips
        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right