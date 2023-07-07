class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['*','/','+','-']

        for token in tokens:
            if token in operators:
                item1 = stack.pop()
                item2 = stack.pop()

                if token == '*':
                    stack.append(item1 * item2)
                elif token == '+':
                    stack.append(item1 + item2)
                elif token == '-':
                    stack.append(item2 - item1)
                else:
                    stack.append(int(item2/item1))
            else:
                stack.append(int(token))

        return stack[-1] if stack else 0