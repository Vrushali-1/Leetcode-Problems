class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left = 0
        answer = 0

        robots = collections.deque()
        runningCost = 0

        for right in range(len(chargeTimes)):
            while robots and robots[-1] < chargeTimes[right]:
                robots.pop()
            robots.append(chargeTimes[right])

            runningCost += runningCosts[right]

            k = right - left + 1

            while robots and robots[0] + (k * runningCost) > budget:
                runningCost -= runningCosts[left]
                if robots[0] == chargeTimes[left]:
                    robots.popleft()
                left += 1
            answer = max(answer,right - left + 1)
        return answer