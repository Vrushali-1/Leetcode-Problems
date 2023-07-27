class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def helper(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        result = 0
        base = 1

        while helper(n + result) > target:
            base *= 10
            result = base - (n % base)
        return result

