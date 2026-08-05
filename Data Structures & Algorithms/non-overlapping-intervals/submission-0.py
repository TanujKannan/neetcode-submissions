'''
[[1,2],[2,4],[1,4]]

prevStart = 1, prevEnd = 2

curStart = 2, curEnd = 4
So prevEnd >= curStart:
    count = 1
    prevStart = 2
    prevEnd = 4

prevStart = 2, prevEnd = 4
curStart, curEnd = 1, 4
So prevEnd >= curStart:
    count = 2
    prevStart = 1
    prevEnd = 4

return count = 2
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        count = 0

        for curStart, curEnd in intervals[1:]:
            if prevEnd > curStart:
                count += 1
                prevEnd = min(prevEnd, curEnd)
            else:
                prevEnd = curEnd
        
        return count
        