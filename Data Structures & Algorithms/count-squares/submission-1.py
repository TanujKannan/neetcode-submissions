class CountSquares:

    def __init__(self):
        self.pointFreq = defaultdict(int)
        self.sameXDiffY = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        x,y = point
        if self.pointFreq[(x,y)] == 0:
            self.sameXDiffY[x].append(y)
        self.pointFreq[(x,y)] += 1
        

    def count(self, point: List[int]) -> int:
        x , y = point
        res = 0

        for secondPointY in self.sameXDiffY[x]:
            count_second = self.pointFreq[(x, secondPointY)]
            if secondPointY == y:
                continue
            
            #Side length
            d = abs(secondPointY - y)

            #Third and fourth, to the right
            count_third_right = self.pointFreq[(x + d, y)]
            count_fourth_right = self.pointFreq[(x + d, secondPointY)]

            res += count_second * count_third_right * count_fourth_right

            #Third and fourth, to the left
            count_third_left = self.pointFreq[(x - d, y)]
            count_fourth_left = self.pointFreq[(x - d, secondPointY)]

            res += count_second * count_third_left * count_fourth_left

        return res

        
