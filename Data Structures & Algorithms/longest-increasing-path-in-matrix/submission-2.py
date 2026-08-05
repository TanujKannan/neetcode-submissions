'''
We want to find the longest strictly increasing path within the matrix.
From each cell, we can move either horizontally or vertically.

We want the longest increasing path at (r,c) where matrix[r][c] is the end of the path.
So if a cell is smaller than all valid neighbors, it has a longest length of 1
with it being the last cell in the path.

State is just r,c
'''
from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix), len(matrix[0])
        @cache
        def recurse(r, c):
            #Default best is 1
            best = 1
            
            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc] < matrix[r][c]:
                    checkNeighbor = recurse(nr, nc)
                    best = max(best, checkNeighbor + 1)
            
            return best
        
        ans = 1
        for r in range(m):
            for c in range(n):
                best_here = recurse(r, c)
                ans = max(ans, best_here)
    
        return ans


        