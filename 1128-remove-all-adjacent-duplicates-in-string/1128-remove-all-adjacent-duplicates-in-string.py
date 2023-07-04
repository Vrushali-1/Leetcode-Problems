class Solution:
    def removeDuplicates(self, s: str) -> str:
        letters = []

        for c in s:
            if not letters:
                letters.append(c)
            else:
                if c == letters[-1]:
                    letters.pop()
                else:
                    letters.append(c)
        return "".join(letters)