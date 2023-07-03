class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(int)
        answer = []
        index = 0

        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))
            if temp not in words:
                words[temp] = index
                index += 1
                answer.append([strs[i]])
            else:
                answer[words[temp]].append(strs[i])
        
        return answer
            