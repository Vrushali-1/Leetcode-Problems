class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = collections.Counter()
        left = 0
        maximumLength = 0

        for i in range(len(s)):
            seen[s[i]] += 1

            while(seen[s[i]] > 1):
                seen[s[left]] -= 1
                left += 1
            maximumLength = max(maximumLength,i-left+1)
        return maximumLength