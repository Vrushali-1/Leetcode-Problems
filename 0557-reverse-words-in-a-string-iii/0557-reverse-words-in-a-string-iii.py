class Solution:
    def reverseWords(self, s: str) -> str:
        spaceIndex = -1
        left = 0
        answer = list(s)
        for right in range(len(s)+1):
            if right == len(s) or s[right] == " ":
                left = spaceIndex + 1
                spaceIndex = right
                currentRight = right - 1   
                while(left<currentRight):
                    answer[currentRight], answer[left] = answer[left],answer[currentRight]
                    currentRight-=1
                    left+=1
        return "".join(answer)
            