class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        startx,starty,empty,pathCount = 0,0,0,0

        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 0:
                    empty += 1
                if grid[i][j] == 1:
                    startx,starty = i,j

        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n
        
        def backtrack(row,col,remain):
            nonlocal pathCount
            if grid[row][col] == 2 and remain == 0:
                pathCount += 1
                return
            
            for dx,dy in directions:
                r,c = row + dx, col + dy
                if isValid(r,c) and grid[r][c] >= 0:
                    temp = grid[row][col]
                    grid[row][col] = -4
                    backtrack(r,c,remain - 1)
                    grid[row][col] = temp
            
        # def backtrack(row, col, remain):
            
        #     nonlocal pathCount

        #     # base case
        #     # print(row,col, remain)
        #     if grid[row][col] == 2 and remain == 0:
        #         pathCount += 1
               
        #         return
            
        #     for x,y in directions:
        #         next_r, next_c= row+x,col+y
        #         if isValid(next_r,next_c) and grid[next_r][next_c]>=0:
        #             temp = grid[row][col] 
        #             grid[row][col] = -4
        #             backtrack(next_r, next_c, remain-1)
        #             grid[row][col] = temp
        
        backtrack(startx,starty,empty - 1)
        return pathCount
        
