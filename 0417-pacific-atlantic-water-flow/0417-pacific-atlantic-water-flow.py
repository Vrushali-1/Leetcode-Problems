class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        m = len(heights)
        n = len(heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row,col,ocean):
            ocean.add((row,col))
            for dx, dy in directions:
                nextRow, nextCol = row + dy, col + dx
                if isValid(nextRow, nextCol) and (nextRow,nextCol) not in ocean and heights[nextRow][nextCol] >= heights[row][col]:
                    dfs(nextRow,nextCol,ocean)
        
        for row in range(m):
            dfs(row,0,pacific)
            dfs(row,n-1,atlantic)
        
        for col in range(n):
            dfs(0,col,pacific)
            dfs(m-1,col,atlantic)
        
        return pacific.intersection(atlantic)





