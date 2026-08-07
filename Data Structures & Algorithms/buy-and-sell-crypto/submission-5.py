'''
given array of prices.
can choose one day to buy a coin and a different day in future to sell it

want to return max profit that can be achieved.

We only care about positive slopes, since that's where profit is.
Buy low sell high

Can use two pointers?
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
        
        return res


        