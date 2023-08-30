class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        seen = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def isValid(row, col):
            return 0 <= row < m and 0<= col < n and board[row][col] == 'O'

        def dfs(row,col):
            seen.add((row,col))
            for dx, dy in directions:
                nextRow, nextCol = row + dy, col + dx
                if isValid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                    dfs(nextRow,nextCol)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        
        for j in range(1,n-1):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)
        
        for row in range(1,m-1):
            for col in range(1,n-1):
                if board[row][col] == 'O' and (row,col) not in seen:
                    board[row][col] = 'X'
        return