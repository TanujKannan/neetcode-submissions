class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid), len(grid[0])
        numIslands = 0
        visited = set()


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue = deque([(i,j)])
                    numIslands += 1

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                            nx = x + dx
                            ny = y + dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                                grid[nx][ny] = "0"
                                queue.append((nx,ny))
        
        return numIslands
        