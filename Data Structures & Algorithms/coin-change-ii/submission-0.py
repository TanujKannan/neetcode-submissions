from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def recurse(i, remaining):
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            
            if i >= n:
                return 0
            
            take = recurse(i , remaining - coins[i])
            skip = recurse(i + 1, remaining)

            return take + skip
    
        return recurse(0 , amount)
        