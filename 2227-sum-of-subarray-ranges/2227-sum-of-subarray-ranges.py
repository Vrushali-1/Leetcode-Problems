class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        n = len(nums)

        #for loop to subtract all maximum values
        for right in range(n + 1):
            while stack and ( right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop() 
                left = -1 if not stack else stack[-1] 
                answer += nums[mid] * (mid - left) * (right - mid) 
            stack.append(right)

        stack.clear()

        # for loop to subtract of all minimum values
        for right in range(n + 1):
            while stack and ( right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()#target index whoose elements's min frequncy needed
                left = -1 if not stack else stack[-1]#from this index the minimum element will not be the same
                answer -= nums[mid] * (mid - left) * (right - mid)# summation
            stack.append(right)     

        return answer