class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        def convert(arr):
            return tuple(arr)
        
        rows = defaultdict(int)

        for row in grid:
            rows[convert(row)] += 1

        columns = defaultdict(int)

        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            columns[convert(column)] += 1
        
        answer = 0
        
        for arr in rows:
            answer += rows[arr] * columns[arr]
        return answer 
            