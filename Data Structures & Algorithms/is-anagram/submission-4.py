'''
Need to check if two strings are anagrams of one another.
Anagram if contain exact same chars, even if diff order.

Need to create two size 26 arrays and compare, after incrementing count
based on index of char. This can only be done since we can safely assume that both strings consist of only lowercase english letters.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        
        for val in arr:
            if val != 0:
                return False
        
        return True
        