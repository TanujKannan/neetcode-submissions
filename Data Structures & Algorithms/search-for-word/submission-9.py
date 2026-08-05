class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board), len(board[0])
        word_len = len(word)

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def backtrack(r , c , i):
            if i == word_len:
                return True
            
            if r<0 or r>=m or c<0 or c>=n or board[r][c] != word[i]:
                return False
            
            char = board[r][c]
            board[r][c] = "#"
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if backtrack(nr, nc, i + 1):
                    return True
            board[r][c] = char
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i , j , 0):
                    return True
        
        return False
                

        