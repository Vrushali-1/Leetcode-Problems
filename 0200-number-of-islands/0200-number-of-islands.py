class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        m = len(grid)
        n = len(grid[0])
        answer = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                if isValid(nextRow,nextCol) and (nextRow,nextCol) not in seen:
                    seen.add((nextRow,nextCol))
                    dfs(nextRow,nextCol)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    answer += 1
                    seen.add((i,j))
                    dfs(i,j)
        
        return answer