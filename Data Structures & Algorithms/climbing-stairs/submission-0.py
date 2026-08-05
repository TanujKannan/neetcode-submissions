from functools import cache
class Solution:
    def climbStairs(self, n):
        @cache
        def recurse(k):
            if k <= 1:
                return 1
            return recurse(k-1) + recurse(k-2)

        return recurse(n)
        