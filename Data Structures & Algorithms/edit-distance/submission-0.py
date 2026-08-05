class Solution:
    def minDistance(self, word1 ,  word2):
        m = len(word1)
        n = len(word2)
        memo = {}
        def recurse(i , j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m:
                return n - j
            if j == n:
                return m - i

            if word1[i] == word2[j]:
                memo[(i,j)] = recurse(i+1, j+1)
                return memo[(i,j)]

            else:
                memo[(i,j)] = 1 + min(recurse(i+1, j), recurse(i, j+1), recurse(i+1, j+1))
                return memo[(i,j)]
    
        return recurse(0, 0)
        