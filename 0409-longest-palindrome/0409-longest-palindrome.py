class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        odd = 0
        result = 0

        for key,freq in counts.items():
            if freq % 2 == 0:
                result += freq
            else:
                odd = 1
                result += freq - 1
        return result + odd