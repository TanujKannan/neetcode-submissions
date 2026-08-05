'''
Given three strings: s1, s2, s3.
We want to know if s3 can be formed by interleaving s1 and s2 together.
s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

This is true, because we do aa + bbbb + aa = s3.
So need two pointers, index for s1 and index for s2.
Do we need an extra index for s3?

Maybe subproblem is:
1. Using s1[:i] and s2[:j], can I get s3[:i+j]?

At any moment, four things are possible:
1. s1[i-1] == s3[i+j-1] -> Shift pointer
2. s2[j-1] == s3[i+j-1] -> Shift pointer
3. Neither of 1 and 2? -> Return False
4. Both s1[i-1] and s2[j-1] == s3[i+j-1]
'''
from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i > 0 and s1[i-1] == s3[i+j-1] and j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
                elif i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
            
                elif j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
        return dp[len(s1)][len(s2)]


        