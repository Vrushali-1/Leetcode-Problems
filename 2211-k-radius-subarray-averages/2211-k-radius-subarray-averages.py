class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)
        addition = 0

        averages = [-1 for i in range(length)]

        if k == 0:
            return nums
        
        if (2 * k + 1) > length:
            return averages
            
        for i in range((2 * k + 1)):
            addition += nums[i]
        averages[k] = addition//(2 * k + 1)

        for i in range((2 * k + 1),length):
            addition = addition + nums[i] - nums [i - (2 * k + 1)]
            averages[i-k] = addition//(2 * k + 1)
        return averages


        

