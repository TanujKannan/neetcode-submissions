class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def replaceSumSquares(num):
            digits = []
            while num > 0:
                digit = num % 10
                digits.append(digit)
                num = num // 10
            res = 0
            for digit in digits:
                res += (digit*digit)
            return res
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = replaceSumSquares(n)
        
        return True