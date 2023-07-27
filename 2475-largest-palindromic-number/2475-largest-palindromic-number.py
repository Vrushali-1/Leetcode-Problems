class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = collections.Counter(num)
        first = ''
        middle = ''

        for digit in range(9,0,-1):
            if counts[str(digit)] >= 2:
                first += str(digit) * (counts[str(digit)]//2)
        
        if first and counts['0'] >= 2:
            first += '0' * (counts['0']//2)
        
        for digit in range(9,-1,-1):
            if counts[str(digit)] % 2 == 1:
                middle = str(digit)
                break
        
        if not first and not middle:
            middle = '0'
        
        return first + middle + first[::-1]