class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkFeasibility(speed):
            total_time = 0
            for pile in piles:
                total_time += (pile + speed - 1)//speed
            if total_time <= h:
                return True
            else:
                return False
            
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r)//2
            if checkFeasibility(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        