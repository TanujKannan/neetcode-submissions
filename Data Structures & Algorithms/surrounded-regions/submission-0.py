class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m , n = len(board) , len(board[0])

        queue = deque([])

        for i in range(m):
            if board[i][0] == "O":
                queue.append((i,0))
                board[i][0] = "#"
            if board[i][n-1] == "O":
                queue.append((i , n-1))
                board[i][n-1] = "#"

        for j in range(n):
            if board[0][j] == "O":
                queue.append((0,j))
                board[0][j] = "#"
            if board[m-1][j] == "O":
                queue.append((m-1 , j))
                board[m-1][j] = "#"   
        
        while queue:
            x , y = queue.popleft()
            for dx , dy in [(0,1), (0,-1), (-1,0), (1,0)]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == "O":
                    board[nx][ny] = "#"
                    queue.append((nx,ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"        

        