from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @cache
        def recurse(index, remaining):
            if index >= n:
                return 0
            
            if remaining == 0:
                return 1
            
            if remaining < 0:
                return 0
            
            skip = recurse(index + 1, remaining)
            take = recurse(index, remaining - coins[index])
            return skip + take
        
        return recurse(0, amount)

        