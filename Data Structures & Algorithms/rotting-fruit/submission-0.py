class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        queue = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j, 0))
        
        res_time = 0

        while queue:
            x , y , time = queue.popleft()
            res_time = time

            for dx , dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx,ny,time+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return res_time
        

        