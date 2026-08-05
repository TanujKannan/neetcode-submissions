class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def checkFeasibility(t):
            queue = deque([(0,0)])
            visited = set()

            while queue:
                x , y = queue.popleft()
                if x == n-1 and y == n-1:
                    return True
                
                for dx , dy in [(0,1), (-1,0), (0,-1), (1,0)]:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]<=t:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            return False
        
        l = max(grid[0][0], grid[n-1][n-1])
        r = n*n - 1

        while l < r:
            mid = (l+r)//2
            if checkFeasibility(mid):
                r = mid
            else:
                l = mid + 1
        return l

        