from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def recurse(i, isHolding):
            if i >= n:
                return 0

            if isHolding:
                sell = prices[i] + recurse(i + 2, 0)
                hold = recurse(i+1, 1)
                return max(sell, hold)
            else:
                buy = -prices[i] + recurse(i+1, 1)
                skip = recurse(i+1, 0)
                return max(buy, skip)
        
        return recurse(0, 0)
        



        