'''
Given two strings s and t, which consist of english letters.

We want to return the number of distinct subsequences of s which are equal to t.

s = "caaat", t = "cat"

Here, answer is 3. We can get cat in three ways from s.

So two pointers, i and j. Prefix approach -> So look backwards.
Two cases:
1. s[i-1] == t[j-1]
2. Not equal -> Then we need to try s[i-1], t[j] and s[i],t[j-1]? Return their sum?

How is this any different from Longest Common Subsequence?
'''
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        @cache
        def recurse(i , j):
            if j == 0:
                return 1
            if i == 0:
                return 0
            
            if s[i-1] == t[j-1]:
                return recurse(i-1, j-1) + recurse(i-1, j)
            else:
                return recurse(i-1, j)
        return recurse(len(s), len(t))
        