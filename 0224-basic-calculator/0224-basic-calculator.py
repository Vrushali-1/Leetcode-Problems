class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        operand = 0
        result = 0

        for c in s:
            if c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            
            elif c== ")":
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                operand = 0
                sign = 1
            
            elif c=="+":
                result += sign * operand
                sign = 1
                operand = 0

            elif c=="-":
                result += sign * operand
                sign = -1
                operand = 0

            elif c.isdigit():
                operand = operand * 10 + int(c)

        return result + sign * operand
