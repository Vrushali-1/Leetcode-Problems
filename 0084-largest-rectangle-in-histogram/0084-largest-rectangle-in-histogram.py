class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maximumArea = 0

        for right in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[right]:
                height = heights[stack.pop()]
                width = right - stack[-1] - 1
                maximumArea = max(maximumArea,(height * width))
            stack.append(right)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            maximumArea = max(maximumArea,(height * width))

        return maximumArea