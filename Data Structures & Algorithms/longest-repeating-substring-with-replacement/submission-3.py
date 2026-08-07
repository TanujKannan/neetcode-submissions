'''
given string - only uppercase
given k

can choose k chars of string and replace them with any other uppercase char

can perform at most k replacements, want length of longest substring
with only one distinct character

so invalid substrings are those where the freq of most occuring char
in the substring > k.

shrink the window till it's valid, then update result.

use freq map and maxFreq
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        maxFreq = 0

        res = 1

        l = 0

        for r in range(len(s)):
            frequencies[s[r]] += 1
            maxFreq = max(maxFreq, frequencies[s[r]])

            while (r - l + 1) - maxFreq > k:
                frequencies[s[l]] -= 1
                l += 1
            
            res = max(res, r - l+1)
        
        return res

        