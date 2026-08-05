'''
We are given the prices of a single coin over multiple days.
We can buy and sell this coin multiple times.
But there are restrictions:
1. After selling the coin, cannot buy the next day.
2. Can only own at most one coin at a time.

Want to return max profit possible.

So I need to know what index I am at and also what state I am in.

So if I am at index i, I can be in one of three states:
1. Buy -> Can go to either sell or hold. At index i + 1.
2. Sell -> Can only go to buy state, at index i + 2. Or do nothing at index i + 1?
3. Hold -> Can either hold or sell, at index i + 1.

Need a do nothing state? How else do I decide if to buy on day 1?

Base cases?
1. If index == len(prices): return 0. Can't make any profit on the last day?

At any given moment, we are either holding nothing or holding a stock.
'''
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def recurse(i, isHolding):
            if i >= n:
                return 0
            if isHolding:
                sell = prices[i] + recurse(i+2, False)
                hold = recurse(i+1, True)
                return max(sell, hold)
            else:
                buy = -prices[i] + recurse(i+1, True)
                holdNothing = recurse(i+1, False)
                return max(buy, holdNothing)
        
        return recurse(0, False)
            

            

        