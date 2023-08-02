class Solution:
	def maximumMinutes(self, grid: List[List[int]]) -> int:
		mx = float('inf')
		m,n = len(grid), len(grid[0])
		arr = [[mx for i in range(n)] for j in range(m)]
		q = deque([(j,i) for i in range(n) for j in range(m) if grid[j][i] == 1])
		for i,j in q:
			arr[i][j] = 0
		visited = set(q)
		temp = 0
		while q:
			l = len(q)
			for j in range(l):
				x,y = q.popleft()
				visited.add((x,y))
				arr[x][y] = temp
				for i,j in (1,0),(0,1),(-1,0),(0,-1):
					xx = x+i
					yy = y+j
					if 0<=xx<m and 0<=yy<n and grid[xx][yy] == 0 and (xx,yy) not in visited:
						q.append((xx,yy))
			temp += 1
		def solve(x,y,temp):
			nonlocal visited
			val = arr[x][y]
			if x == m-1 and y == n-1:
				return temp <= val
			visited.add((x,y))
			if val <= temp:return False
			for i,j in (1,0),(0,1),(-1,0),(0,-1):
				xx = x+i
				yy = y+j
				if 0<=xx<m and 0<=yy<n and (xx,yy) not in visited and grid[xx][yy] != 2:
					if solve(xx,yy, temp+1):
						return True
			# visited.remove((x,y))
			return False

		# for row in arr:
		#     print(*row)
		visited = set()
		if not solve(0,0,0):return -1
		l,r = 0,10**9
		ans = None
		while l <= r:
			mid = (l+r)//2
			visited = set()
			if solve(0,0,mid):
				ans = mid
				l = mid+1
			else:
				r = mid-1
		return ans