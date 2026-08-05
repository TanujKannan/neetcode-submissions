from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        @cache
        def recurse(i , j):
            if i == 0:
                return 0
            if j == 0:
                return 0
            
            if text1[i-1] == text2[j-1]:
                return 1 + recurse(i-1,j-1)
            else:
                return max(recurse(i-1, j), recurse(i, j -1))
    
        return recurse(m, n)
        