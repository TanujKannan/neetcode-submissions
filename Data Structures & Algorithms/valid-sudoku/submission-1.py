class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        subBox = [0]*9


        m , n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                
                value = int(board[r][c]) - 1
                mask = (1 << value)

                if (mask & rows[r]) or (mask & cols[c]) or (mask & subBox[(r//3)*3 + c//3]):
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                subBox[(r//3)*3 + c//3] |= mask
        
        return True
        