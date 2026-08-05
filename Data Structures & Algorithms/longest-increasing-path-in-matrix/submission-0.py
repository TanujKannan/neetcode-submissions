from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix):
        m , n  = len(matrix), len(matrix[0])
        @cache
        def recurse(r , c):
            best = 1
            for dr , dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<m and 0<=nc<n and matrix[r][c] > matrix[nr][nc]:
                    best = max(best, 1 + recurse(nr, nc))
            
            return best
    
        return max(recurse(r,c) for r in range(m) for c in range(n))
    
        