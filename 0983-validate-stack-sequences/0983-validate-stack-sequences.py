class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popIndex = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]== popped[popIndex]:
                stack.pop()
                popIndex += 1
        while stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1
        
        return not stack