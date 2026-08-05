class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board), len(board[0])
        l = len(word)

        def recurse(r , c, i):
            if i == l:
                return True
            
            if r<0 or r>=m or c<0 or c>=n or i > l or board[r][c] != word[i]:
                return False
            
            char = board[r][c]
            board[r][c] = "#"
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                if recurse(nr, nc, i+1):
                    return True
            
            board[r][c] = char
            return False
    
        for i in range(m):
            for j in range(n):
                if recurse(i , j, 0):
                    return True
        
        return False


        