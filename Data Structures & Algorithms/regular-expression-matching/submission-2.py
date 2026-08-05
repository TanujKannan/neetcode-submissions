from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recurse(i , j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            #Check if there's a match between current chars
            match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')

            if j+1 < len(p) and p[j + 1] == "*":
                return recurse(i , j+2) or (match and recurse(i+1, j))
            
            if match:
                return recurse(i+1, j+1)
            
            return False
        
        return recurse(0,0)



        