class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [[p,s] for p,s in zip(position,speed)]

        for i,c in sorted(pair)[::-1]:
            distance = target - i
            time = distance/c
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
            