class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        answer = 0
        for i in range(len(arr)):
            if arr[i] + 1 in nums:
                answer += 1
        return answer