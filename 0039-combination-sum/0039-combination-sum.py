class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,path,currentSum):
            if currentSum == target:
                answer.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                num = candidates[i]
                if num + currentSum <= target:
                    path.append(num)
                    backtrack(i,path,currentSum + num)
                    path.pop()
        
        answer = []
        backtrack(0,[],0)
        return answer