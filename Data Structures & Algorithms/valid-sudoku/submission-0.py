class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        subGrid = [0]*9

        m , n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                
                value = int(board[i][j]) - 1
                mask = (1 << value)

                if (mask & rows[i] or mask & cols[j] or mask & subGrid[(i//3)*3 + j//3]):
                    return False
                
                rows[i] |= mask
                cols[j] |= mask
                subGrid[(i//3)*3 + j//3] |= mask
        
        return True
        