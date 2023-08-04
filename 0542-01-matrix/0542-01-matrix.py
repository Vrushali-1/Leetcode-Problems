class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen = set()
        queue = collections.deque()
        m = len(mat)
        n = len(mat[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def isValid(row,col):
            return 0 <= row < m and 0 <= col < n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen.add((i,j))
                    queue.append((i,j,1))
        
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                nextRow = row + dx
                nextCol = col + dy
                if isValid(nextRow,nextCol) and (nextRow, nextCol) not in seen:
                    queue.append((nextRow,nextCol, steps + 1))
                    seen.add((nextRow, nextCol))
                    mat[nextRow][nextCol] = steps
        
        return mat

        
        
