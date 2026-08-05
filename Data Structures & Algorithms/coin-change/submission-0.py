from functools import cache
class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        @cache
        def recurse(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            min_coins = float('inf')
            for c in coins:
                min_coins = min(min_coins , 1 + recurse(remaining - c))

            return min_coins

        ans = recurse(amount)
        return -1 if ans == float('inf') else ans
        