from functools import cache
class Solution:
    def numDistinct(self, s ,  t):
        m = len(s)
        n = len(t)
        @cache
        def recurse(i , j):
            if j == n:
                return 1
            if i == m:
                return 0

            if s[i] == t[j]:
                take = recurse(i+1,  j+1)
                skip = recurse(i+1, j)
                return take + skip
            else:
                return recurse(i+1, j)
    
        return recurse(0, 0)
        