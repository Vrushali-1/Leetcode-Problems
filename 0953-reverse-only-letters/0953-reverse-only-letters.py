class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        right = len(s) - 1
        ans = []
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[right].isalpha():
                    right -= 1
                ans.append(s[right])
                right -= 1
            else:
                ans.append(s[i])
        return "".join(ans)
