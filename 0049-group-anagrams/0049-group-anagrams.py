class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))
            words[temp].append(strs[i])
        
        return words.values()
            