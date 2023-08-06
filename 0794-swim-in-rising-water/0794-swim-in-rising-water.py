class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def check(time_limit):
            stack = [(0, 0)]
            visited = {(0, 0)}

            while stack:
                row, col = stack.pop()

                if row == col == n - 1:
                    return True
                    
                for nrow, ncol in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (0 <= nrow < n and 0 <= ncol < n
                            and (nrow, ncol) not in visited and grid[nrow][ncol] <= time_limit):
                        stack.append((nrow, ncol))
                        visited.add((nrow, ncol))
            return False

        n = len(grid)
        left,right = grid[0][0], n * n

        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left