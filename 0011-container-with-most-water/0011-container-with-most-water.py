class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        right = len(height) - 1
        length = 0
        breadth = 0
        left = 0
        while(left < right):
            length = right - left
            if height[left] < height[right]:
                breadth = height[left]
                left += 1
            else:
                breadth = height[right]
                right -= 1
            if area < length * breadth:
                area = length * breadth
        return area