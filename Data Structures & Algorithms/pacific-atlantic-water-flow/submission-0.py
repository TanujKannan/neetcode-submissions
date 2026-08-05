class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n = len(heights), len(heights[0])

        pac_queue = deque([])
        atl_queue = deque([])

        visited_pac = set()
        visited_atl = set()

        for i in range(m):
            pac_queue.append((i, 0))
            visited_pac.add((i,0))
            atl_queue.append((i , n - 1))
            visited_atl.add((i,n-1))
        
        for j in range(n):
            if (0 , j) not in visited_pac:
                pac_queue.append((0 , j))
                visited_pac.add((0,j))
            if (m-1, j) not in visited_atl:
                atl_queue.append((m-1, j))
                visited_atl.add((m-1,j))


        while pac_queue:
            x , y = pac_queue.popleft()

            for dx, dy in [(0,1), (-1,0), (1,0), (0,-1)]:
                nx = dx + x
                ny = dy + y
                if 0<=nx<m and 0<=ny<n and heights[nx][ny] >= heights[x][y] and (nx,ny) not in visited_pac:
                    pac_queue.append((nx,ny))  
                    visited_pac.add((nx,ny))  

        while atl_queue:
            x , y = atl_queue.popleft()

            for dx, dy in [(0,1), (-1,0), (1,0), (0,-1)]:
                nx = dx + x
                ny = dy + y
                if 0<=nx<m and 0<=ny<n and heights[nx][ny] >= heights[x][y] and (nx,ny) not in visited_atl:
                    atl_queue.append((nx,ny))  
                    visited_atl.add((nx,ny)) 

        return list(visited_atl & visited_pac)     
        