from functools import cache
class Solution:
    def uniquePaths(self, m, n):
        @cache
        def recurse(r , c):
            if r == 0:
                return 1
            if c == 0:
                return 1
            
            fromAbove = recurse(r-1, c)
            fromLeft = recurse(r , c-1)

            return fromAbove + fromLeft
    
        return recurse(m-1, n-1)
        