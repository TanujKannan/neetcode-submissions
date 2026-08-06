'''
need to check if palindrome
just need to deal with annoying casing and alphanum

so strip all non alphanum before the two pointer logic?
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for ch in s:
            if ch.isalnum():
                stripped += ch
        
        print(stripped)

        l = 0
        r = len(stripped) - 1

        while l < r:
            if stripped[l].lower() != stripped[r].lower():
                return False
            l+=1
            r-=1
        
        return True

        