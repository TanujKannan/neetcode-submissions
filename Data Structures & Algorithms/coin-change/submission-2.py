from functools import cache
class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if amount - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
        