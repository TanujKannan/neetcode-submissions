class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT = [0]*26
        countS = [0]*26

        if len(s) != len(t):
            return False


        for i in range(len(s)):
            countS[ord(s[i]) - ord('a')] += 1
        
        for j in range(len(t)):
            countT[ord(t[j]) - ord('a')] += 1
        
        print(countS)
        print(countT)
        return countT == countS
        