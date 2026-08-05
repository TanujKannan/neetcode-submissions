from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        @cache
        def recurse(i , j):
            if i == 0 or j == 0:
                return 0
            
            if text1[i-1] == text2[j-1]:
                prev = recurse(i-1, j-1)
                return prev + 1
            
            else:
                return max(recurse(i,j-1), recurse(i-1,j))

        return recurse(l1, l2)        