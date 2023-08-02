class Solution:
	def maximumMinutes(self, grid):
		m, n = len(grid), len(grid[0])
		queue, fireReached = collections.deque(), [[float("inf")] * n for _ in range(m)]
		directions = [(1,0),(0,1),(-1,0),(0,-1)]

		def isValid(row,col):
			return 0 <= row < m and 0 <= col < n and grid[row][col] == 0

		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					queue.append((i,j,0))
					fireReached[i][j] = 0
		
		while queue:
			row,col,time = queue.popleft()

			for dx, dy in directions:
				x,y = row + dy, col + dx

				if isValid(x,y) and fireReached[x][y] > time + 1:
					fireReached[x][y] = time + 1
					queue.append((x,y,time + 1))
		
		def check(time):
			queue, visited = collections.deque([(0,0,time)]), [[0] * n for _ in range(m)]

			while queue:
				row,col,t = queue.popleft()

				for dx,dy in directions:
					x,y = row + dy, col + dx

					if x == m - 1 and y == n - 1 and t + 1 <= fireReached[x][y]:
						return True
					
					if isValid(x,y) and visited[x][y] == 0 and t+1 < fireReached[x][y]:
						queue.append((x,y,t+1))
						visited[x][y] = 1
			return False
		
		low,high = 0, 10 ** 9

		while low <= high:
			mid = (low + high) // 2
			if check(mid):
				low = mid + 1
			else:
				high = mid - 1
		return high
