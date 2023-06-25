class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        index = -1
        for i in range(len(word)):
            if word[i] == ch:
               index = i
               break
        if index==-1:
            return word
        answer = list(word)
        right = index
        while left < right:
            temp = answer[right]
            answer[right] = answer[left]
            answer[left] = temp
            right -= 1
            left += 1
        return "".join(answer)