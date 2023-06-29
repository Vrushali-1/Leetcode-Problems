class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        set1 = set(count1.keys())
        set2 = set(count2.keys())

        one = sorted(count1.values())
        two = sorted(count2.values())

        return set1 == set2 and one==two