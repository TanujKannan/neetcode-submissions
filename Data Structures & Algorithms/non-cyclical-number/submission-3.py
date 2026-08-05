class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def replaceSumSquares(num):
            res = 0
            while num > 0:
                digit = num % 10
                res += digit*digit
                num = num // 10
            return res

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = replaceSumSquares(n)
        
        return True