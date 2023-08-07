class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def check(value,start):
            left = start
            right = len(nums2) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] < value:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        answer = 0
        
        for i,num in enumerate(nums1):
            if i >= len(nums2):
                break
            if num > nums2[i]:
                continue
            
            end = check(num,i)
            answer = max(answer,end - i)
        return answer