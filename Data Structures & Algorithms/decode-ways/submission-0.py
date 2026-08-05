from functools import cache
class Solution:
    def numDecodings(self, s):
        n = len(s)
        @cache
        def recurse(i):
            if i == 0:
                return 1
        
            if i == 1:
                return 0 if s[0] == "0" else 1
            
            ways = 0
            if s[i-1] != "0":
                ways += recurse(i - 1)
            
            if 10<=int(s[i-2:i])<=26:
                ways += recurse(i - 2)
            
            return ways
        return recurse(n)
        