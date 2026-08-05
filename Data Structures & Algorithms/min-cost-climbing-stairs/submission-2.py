from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        a = cost[0]
        b = cost[1]

        for i in range(2, n):
            cur = cost[i] + min(a,b)
            a = b
            b = cur

        return min(a, b)
        