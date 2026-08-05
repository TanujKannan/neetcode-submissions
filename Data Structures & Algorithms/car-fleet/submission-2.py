class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for p, s in zip(position , speed):
            pairs.append((p, s))
        
        pairs.sort(reverse = True)

        #Time = Distance / speed
        prevTime = (target - pairs[0][0])/pairs[0][1]

        fleets = 1

        for pos, s in pairs[1:]:
            curTime = (target - pos)/s
            if curTime > prevTime:
                fleets += 1
                prevTime = curTime
        
        return fleets


        