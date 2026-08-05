from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        @cache
        def recurse(k):
            if k == 0:
                return cost[0]
            if k == 1:
                return cost[1]
            return min(recurse(k-1), recurse(k-2)) + cost[k]

        return min(recurse(n-1), recurse(n-2))
        