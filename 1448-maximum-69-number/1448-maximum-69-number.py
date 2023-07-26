class Solution:
    def maximum69Number (self, num: int) -> int:
        chars = list(str(num))
        
        for i,digit in enumerate(chars):
            if digit == '6':
                chars[i] = '9'
                break
        return int("".join(chars))