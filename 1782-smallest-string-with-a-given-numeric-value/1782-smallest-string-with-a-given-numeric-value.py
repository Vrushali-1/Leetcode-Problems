class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a' for _ in range(n)]
        k = k - n
        i = n - 1
        while k:
            k += 1
            if k/26 >= 1:
                result[i], k, i = 'z', k - 26, i - 1
            else:
                result[i],k= chr(k + 96), 0
        return "".join(result)