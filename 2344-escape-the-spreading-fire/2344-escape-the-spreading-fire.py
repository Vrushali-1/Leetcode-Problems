class Solution:
	def maximumMinutes(self, grid):
		m, n = len(grid), len(grid[0])
		queue, fireReached = [], [[float("inf")] * n for _ in range(m)]
		directions = [(1,0),(0,1),(-1,0),(0,-1)]

		def isValid(row,col):
			return 0 <= row < m and 0 <= col < n and grid[row][col] == 0

		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					queue.append((i,j,0))
					fireReached[i][j] = 0
		
		while queue:
			row,col,time = queue.pop(0)

			for dx, dy in [(row - 1,col),(row + 1,col),(row,col-1),(row,col+1)]:
				#nextRow, nextCol = row + dy, col + dx

				if isValid(dx,dy) and fireReached[dx][dy] > time + 1:
					fireReached[dx][dy] = time + 1
					queue.append((dx,dy,time + 1))
		
		def check(time):
			queue, visited = [(0,0,time)], [[0] * n for _ in range(m)]

			while queue:
				row,col,t = queue.pop(0)

				for dx,dy in [(row - 1,col),(row + 1,col),(row,col-1),(row,col+1)]:
					#nextRow, nextCol = row + dy, col + dx

					if dx == m - 1 and dy == n - 1 and t + 1 <= fireReached[dx][dy]:
						return True
					
					if isValid(dx,dy) and visited[dx][dy] == 0 and t+1 < fireReached[dx][dy]:
						queue.append((dx,dy,t+1))
						visited[dx][dy] = 1
			return False
		
		low,high = 0, 10 ** 9

		while low <= high:
			mid = (low + high) // 2
			if check(mid):
				low = mid + 1
			else:
				high = mid - 1
		return high
