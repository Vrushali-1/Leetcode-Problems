class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    result += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        result -= 2

                    if col > 0 and grid[row][col - 1] == 1:
                        result -= 2
        return result 
