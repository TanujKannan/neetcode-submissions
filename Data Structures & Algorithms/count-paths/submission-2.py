from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def recurse(i , j):
            if i == 0 or j == 0:
                return 1
            
            up = recurse(i-1, j)
            left = recurse(i , j-1)
            return up + left
        
        return recurse(m-1, n-1)
        