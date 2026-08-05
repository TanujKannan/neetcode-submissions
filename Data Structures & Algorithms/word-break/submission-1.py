class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        max_len = max(len(w) for w in words)

        #What's the base case? Empty string is True.
        dp[0] = True

        for i in range(1,n+1):
            for j in range(i - max_len, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
    
        return dp[n]
        