class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr,start):
            if start > len(nums):
                return
            answer.append(curr[:])
    
            for i in range(start,len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(curr,i + 1)
                curr.pop()
    
        answer = []
        nums.sort()
        backtrack([],0)
        return answer