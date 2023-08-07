class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(row,col):
            return 0 <= row < m and 0 <= col <n
        def backtrack(i,visited,row,col):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                r,c = row + dy, col + dx
                if isValid(r,c) and (r,c) not in visited:
                    if board[r][c] == word[i]:
                        visited.add((r,c))
                        if backtrack(i + 1, visited,r,c):
                            return True
                        visited.remove((r,c))
            return False
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(board), len(board[0])

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(1,{(row,col)},row,col):
                    return True
        return False
