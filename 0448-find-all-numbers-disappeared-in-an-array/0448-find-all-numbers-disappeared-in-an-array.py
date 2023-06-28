class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        numbers = set(nums)
        for i in range(1,len(nums)+1):
            if i not in numbers:
                answer.append(i)
        return answer