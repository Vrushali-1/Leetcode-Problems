class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximumLength = 0
        maximumCharacter = s[0]
        frequencyMap = collections.Counter()

        left = 0
        for right in range(len(s)):
            frequencyMap[s[right]] += 1

            if frequencyMap[s[right]] > frequencyMap[maximumCharacter]:
                maximumCharacter = s[right]

            windowLength = right - left + 1

            if windowLength - frequencyMap[maximumCharacter] > k:
                frequencyMap[s[left]] -= 1
                left += 1
            maximumLength = max(maximumLength,right - left + 1)
        return maximumLength