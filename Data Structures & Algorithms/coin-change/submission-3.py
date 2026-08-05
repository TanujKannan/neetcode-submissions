'''
At any moment, I can choose to either take the coin I am at or not.
If I take -> I need to find min for coins to make target - coin
If I don't -> I need to find min for same target.

What states do I need to track? Just index? Or just amount left? Or both?

'''
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def recurse(remaining):
            if remaining == 0:
                return 0
            res = float('inf')
            for coin in coins:
                if coin <= remaining:
                    take = recurse(remaining - coin) + 1
                    res = min(res, take)
            return res
        return -1 if recurse(amount) == float('inf') else recurse(amount)


        