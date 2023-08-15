class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,current):
            if start == len(nums):
                if len(current) >= 2:
                    answer.add(tuple(current))
                return
        
            if not current or current[-1]<=nums[start]:
                current.append(nums[start])
                backtrack(start+1,current)
                current.pop()
            backtrack(start+1,current)
    
        answer = set()
        backtrack(0,[])
        return answer