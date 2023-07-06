class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            flag = 1
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) > abs(asteroid):
                    flag = 0
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    flag = 0
                    break
            if flag == 1:
                stack.append(asteroid) 
        return stack


