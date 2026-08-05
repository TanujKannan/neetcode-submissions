from functools import cache
class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0]*(n+1)
        prevTwo = 1
        prevOne = 0 if s[0] == "0" else 1

        for i in range(2, n+1):
            current = 0
            if s[i-1] != "0":
                current += prevOne
            
            if 10<=int(s[i-2:i])<=26:
                current += prevTwo
        
            prevTwo = prevOne
            prevOne = current
        
        return prevOne
        