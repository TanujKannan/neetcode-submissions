'''



'''
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        @cache
        def recurse(i):
            if i == 0:
                return True
            
            for j in range(i):
                checkPrev = recurse(j)
                if checkPrev and s[j:i] in wordSet:
                    return True
            return False
        
        return recurse(n)
            
            

        