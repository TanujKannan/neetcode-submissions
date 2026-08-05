class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevOne = cost[0]
        prevTwo = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(prevOne, prevTwo)
            prevOne = prevTwo
            prevTwo = cur
        
        return min(prevOne, prevTwo)
        