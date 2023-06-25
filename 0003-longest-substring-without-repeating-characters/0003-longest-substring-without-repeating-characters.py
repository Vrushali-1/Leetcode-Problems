class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = collections.Counter()
        left = 0
        maximumLength = 0

        # for i in range(len(s)):
        #     seen[s[i]] += 1

        #     while(seen[s[i]] > 1):
        #         seen[s[left]] -= 1
        #         left += 1
        #     maximumLength = max(maximumLength,i-left+1)
        # return maximumLength

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] + 1 > left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            maximumLength = max(maximumLength,right-left+1)
        return maximumLength 