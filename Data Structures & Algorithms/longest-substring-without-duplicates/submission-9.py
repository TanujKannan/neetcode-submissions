'''
given string s, want to find length of longest substring without duplicate chars.

use a set to maintain chars in the window.
we want longest, so we shrink from left while right char in the set
once valid, update max length
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1

        seen = set()

        l = 0
        seen.add(s[l])

        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l+1)
            seen.add(s[r])
        
        return res
        




