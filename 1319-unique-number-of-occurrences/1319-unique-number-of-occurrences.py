class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter()

        for i in arr:
            counts[i] += 1
        
        numbers = set(counts.values())

        return len(numbers) == len(counts)
