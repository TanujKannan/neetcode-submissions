'''
Need to check if two strings are anagrams of one another.
Anagram if contain exact same chars, even if diff order.

Need to create two size 26 arrays and compare, after incrementing count
based on index of char. This can only be done since we can safely assume that both strings consist of only lowercase english letters.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrT = [0]*26
        arrS = [0]*26

        for ch in s:
            arrS[ord(ch) - ord('a')] += 1
        
        for ch in t:
            arrT[ord(ch) - ord('a')] += 1
        
        return arrS == arrT
        