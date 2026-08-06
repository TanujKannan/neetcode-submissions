'''
Given 9x9 sudoku board. Need to check validity.
Valid if:
1. Each row must contain 1-9 without dups
2. Each column must contain the digits 1-9 without dups
3. Each of 9 3x3 boxes must contain 1-9 without dups

All elements are either 1-9 or '.'

I can use 3 arrays, where each index represents a flag of
whether that number has been seen in the given row/col/sub-box.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        sub_box = [0]*9 #Need to figure out indexing

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c])
                index = val - 1
                box = (r//3)*3 + (c//3)

                mask = 1 << index
                print("mask", mask)
                print("row mask", rows)
                print("col mask", cols)
                print("sub_box", sub_box)

                if rows[r] & mask or cols[c] & mask or sub_box[box] & mask:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                sub_box[box] |= mask
        
        return True


        