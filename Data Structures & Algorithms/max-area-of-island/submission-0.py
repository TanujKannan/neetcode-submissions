class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = deque([(i,j)])
                    grid[i][j] = 0
                    island_count = 0

                    while queue:
                        x , y = queue.popleft()
                        island_count += 1

                        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                            nx = x + dx
                            ny = y + dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                                queue.append((nx,ny))
                                grid[nx][ny] = 0
                    max_area = max(max_area, island_count)
    
        return max_area
        