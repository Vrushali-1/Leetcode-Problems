class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = collections.Counter()
        current = answer = left = 0

        for right in range(len(nums)):
            current += nums[right]

            counts[nums[right]] += 1

            while counts[nums[right]] > 1:
                current -= nums[left]
                counts[nums[left]] -= 1
                left += 1
            
            answer = max(current,answer)
        
        return answer

        # prefix = [0  for i in range(len(nums) + 1)]
        # for i in range(1,len(nums)+1):
        #     prefix[i] = prefix[i - 1] + nums [i - 1]

        # for right in range(len(nums)):

        #     current = nums[right + 1] - nums[left]


        #     if nums[right] in counts:
        #         left = max(left,counts[nums[right]])
        #         current -= prefix[left]
        #     counts[nums[right]] = right + 1

        #     answer = max(answer,current)
        # return answer
