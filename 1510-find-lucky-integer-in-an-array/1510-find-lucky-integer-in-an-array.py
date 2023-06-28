class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        numbers = collections.Counter()

        for i in range(len(arr)):
            numbers[arr[i]] += 1
        
        for i in range(len(arr)):
            if arr[i] == numbers[arr[i]]:
                answer = max(answer,arr[i])
        return answer