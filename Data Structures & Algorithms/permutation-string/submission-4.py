'''
given two strings s1 and s2

need to return if s2 contains a permutation of s1

so if permutation of s1 exists as a substring of s2, return true

both contain only lowercase

if given just two strings, check permutation by comparing character count arrays.

we would only check windows of size len(s1)

if window does have right length, compare the character arrays.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charArrayS1 = [0]*26
        charArrayS2 = [0]*26


        for ch in s1:
            charArrayS1[ord(ch) - ord('a')] += 1
        
        l = 0

        for r in range(len(s2)):
            charArrayS2[ord(s2[r]) - ord('a')] += 1

            while (r - l + 1) > len(s1):
                charArrayS2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if charArrayS2 == charArrayS1:
                return True
        
        return False
        