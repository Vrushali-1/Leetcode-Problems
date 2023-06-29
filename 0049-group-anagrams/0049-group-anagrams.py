class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        answer = []
        words = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            words[key].append(word)

        return words.values()