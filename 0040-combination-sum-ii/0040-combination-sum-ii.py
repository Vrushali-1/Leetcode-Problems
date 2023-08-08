class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(combination,start,counter,remaining):
            if remaining == 0:
                answer.append(combination[:])
                return
            
            elif remaining < 0:
                return
            
            for i in range(start,len(counter)):
                candidate, freq = counter[i]

                if freq <= 0:
                    continue
                
                combination.append(candidate)
                counter[i] = (candidate,freq - 1)
                backtrack(combination,i,counter,remaining - candidate)
                counter[i] = (candidate,freq)
                combination.pop()
        
        answer = []
        nums = collections.Counter(candidates)
        counter = [(c,nums[c]) for c in nums]
        backtrack([],0,counter,target)
        return answer