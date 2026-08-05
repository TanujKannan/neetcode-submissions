class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        nonAlphaS = ""
        for ch in lowerS:
            if ch.isalnum():
                nonAlphaS += ch
        print(nonAlphaS)
        l = 0
        r = len(nonAlphaS) - 1

        while l < r:
            if nonAlphaS[l] != nonAlphaS[r]:
                return False
            l+=1
            r-=1
        
        return True
        