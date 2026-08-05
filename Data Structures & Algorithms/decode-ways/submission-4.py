'''
number of ways to decode at index i depends on:
1. number of ways to decode i - 1 -> If it's not a 0
2. number of ways to decode i - 2 -> If it's between 10 and 26

During recursion, base cases?
1. If i = 0, return 1
2. If i = 1, return 1?
'''
from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        @cache
        def recurse(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            cur_res = 0
            if s[i-1] != "0":
                cur_res += recurse(i-1)
            if 10<=int(s[i-2:i])<=26:
                cur_res += recurse(i-2)
            return cur_res
    
        return recurse(len(s))
            



        