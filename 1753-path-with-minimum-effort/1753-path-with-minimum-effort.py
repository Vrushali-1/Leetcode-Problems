class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n
        
        def check(effort):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            seen = {(0,0)}
            stack = [(0,0)]

            while stack:
                row,col = stack.pop()

                if row == m -1 and col == n -1:
                    return True
                
                for dx,dy in directions:
                    nextRow, nextCol = row + dy, col + dx
                    if isValid(nextRow, nextCol) and (nextRow,nextCol) not in seen:
                        if abs(heights[nextRow][nextCol] - heights[row][col]) <= effort:

                            seen.add((nextRow,nextCol))
                            stack.append((nextRow,nextCol))
            return False
        

        # m, n = len(heights), len(heights[0])
        # left = 0
        # right = max(max(row) for row in heights)

        # while left <= right:
        #     mid = (left + right) // 2

        #     if check(mid):
        #         right = mid - 1
        #     else:
        #         left = left + 1
        # return 
        
        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left