class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        prevOne = 1
        prevTwo = 1

        for i in range(2, n+1):
            cur = prevOne + prevTwo
            prevOne = prevTwo
            prevTwo = cur
        
        return prevTwo