class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popIndex = 0
        for num in pushed:
            stack.append(num)
            
            print(stack[-1])
            print(popped[popIndex])
            while stack and stack[-1]== popped[popIndex]:
                stack.pop()
                popIndex += 1
        print(stack)
        while stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1
        
        return not stack