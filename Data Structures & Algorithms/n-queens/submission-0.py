class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_diag = set()
        neg_diag = set()
        cols = set()

        res = []
        board = [["."]*n for i in range(n)]

        def solve(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return 
            
            for c in range(n):
                if c in cols or (row+c) in pos_diag or (row-c) in neg_diag:
                    continue
                
                pos_diag.add((row + c))
                cols.add(c)
                neg_diag.add((row - c))
                board[row][c] = "Q"

                solve(row + 1)

                pos_diag.remove((row+c))
                cols.remove(c)
                neg_diag.remove((row - c))
                board[row][c] = "."
        
        solve(0)
        return res
            



        