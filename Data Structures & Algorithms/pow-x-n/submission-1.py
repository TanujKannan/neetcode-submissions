class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            if n == 0:
                return 1
            tmp = recurse(x, n//2)
            res = tmp*tmp
            if n % 2 == 1:
                res *= x
            return res
        
        if n >= 0:
            return recurse(x, n)
        else:
            return 1/recurse(x,-n)

        