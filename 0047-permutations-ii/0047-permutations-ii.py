class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current,numbers):
            if len(current) == len(nums):
                answer.append(current[:])
                return
            
            for num in numbers:
                if numbers[num] > 0:
                    current.append(num)
                    numbers[num] -= 1
                    backtrack(current,numbers)
                    current.pop()
                    numbers[num] += 1
        
        answer = []
        backtrack([],collections.Counter(nums))
        return answer