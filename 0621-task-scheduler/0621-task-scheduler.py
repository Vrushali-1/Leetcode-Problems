class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0 for _ in range(26)]

        for task in tasks:
            index = ord(task) - ord('A')
            counts[index] += 1
 
        counts.sort()

        maximum = counts.pop()
        idleTime = (maximum - 1) * n

        while idleTime > 0 and counts:
            idleTime -= min(maximum - 1, counts.pop())
        idleTime = max(0, idleTime)

        return idleTime + len(tasks)