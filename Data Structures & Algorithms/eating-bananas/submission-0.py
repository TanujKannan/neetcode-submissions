class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkFeasibility(k):
            total_time = 0
            for pile in piles:
                total_time += (pile + k - 1)//k
            return total_time <= h
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2
            if checkFeasibility(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        