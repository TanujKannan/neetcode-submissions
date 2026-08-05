from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded_nums = [1] + nums + [1]
        n = len(padded_nums)
        @cache
        def recurse(l , r):
            if l == r - 1:
                return 0
            max_coins = 0
            for k in range(l+1, r):
                popped = (padded_nums[l]*padded_nums[k]*padded_nums[r]) + recurse(l,k) + recurse(k, r)
                max_coins = max(max_coins, popped)
            return max_coins
        
        return recurse(0, n-1)
        