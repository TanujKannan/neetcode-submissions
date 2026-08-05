class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for p, s in zip(position, speed):
            pairs.append((p, s))
        
        pairs.sort(reverse = True)

        prevTime = (target - pairs[0][0]) / pairs[0][1]
        fleets = 1

        for position, speed in pairs[1:]:
            arrivalTime = (target - position) / speed

            if arrivalTime > prevTime:
                fleets += 1
                prevTime = arrivalTime
            
        return fleets
        