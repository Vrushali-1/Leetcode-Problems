class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        answer = []
        words = collections.Counter()

        for word in strs:
            s = ''.join(sorted(word))

            if s in words:
                answer[words[s]].append(word)
            else:
                words[s] = index
                index += 1
                answer.append([word])
        return answer