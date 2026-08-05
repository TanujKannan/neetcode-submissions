from functools import cache
class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        a = 1
        b = 1

        for i in range(2, n+1):
            a , b = b , a + b
        return b
        