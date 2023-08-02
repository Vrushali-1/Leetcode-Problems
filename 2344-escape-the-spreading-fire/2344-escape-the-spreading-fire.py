class Solution:
    def maximumMinutes(self, grid):
        m,n = len(grid),len(grid[0])

        fires, dist = [], [[float("inf")]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append((i,j,0))
                    dist[i][j] = 0

        while fires:
            x,y,t = fires.pop(0)

            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx <= m-1 and 0 <= ny <= n-1 and grid[nx][ny] == 0 and dist[nx][ny] > t+1:
                    dist[nx][ny] = t+1
                    fires.append((nx,ny,t+1))

        def is_possible(t): 
            stack, visited = [(0,0,t)], [[0]*n for _ in range(m)]

            while stack:
                x,y,val = stack.pop(0)

                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if nx == m-1 and ny == n-1 and val+1 <= dist[nx][ny]:
                        return True

                    if 0 <= nx <= m-1 and 0 <= ny <= n-1 and grid[nx][ny] == 0 and visited[nx][ny] == 0 and val+1 < dist[nx][ny]:
                        stack.append((nx,ny,val+1))
                        visited[nx][ny] = 1

            return False

        low, high = 0, 10**9

        while low <= high:
            mid = (low+high)//2

            if is_possible(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high










        