class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def isValid(row,col):
            return 0 <= row < n and 0 <= col < n
        
        def check(height):
            stack = [(0,0)]
            visited = set()
            visited.add((0,0))

            while stack:
                row,col = stack.pop()

                if row == n - 1 and col == n - 1:
                    return True

                for dx,dy in directions:
                    r, c = row + dy, col + dx
                    if isValid(r,c) and (r,c) not in visited and grid[r][c] <= height:
                        stack.append((r,c))
                        visited.add((r,c))
            return False
        
        n = len(grid)
        left,right = grid[0][0], n * n
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left