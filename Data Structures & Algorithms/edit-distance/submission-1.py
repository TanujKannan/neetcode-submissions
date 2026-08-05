from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def recurse(i , j):
            if i == 0:
                return j
            if j == 0:
                return i
            
            if word1[i-1] == word2[j-1]:
                return recurse(i-1, j-1)
            else:
                return 1 + min(recurse(i-1, j-1), recurse(i, j-1), recurse(i-1, j))

        return recurse(len(word1), len(word2))
        