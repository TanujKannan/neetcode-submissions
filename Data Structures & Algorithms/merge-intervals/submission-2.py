class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x:x[0])
        res.append(intervals[0])

        for curStart, curEnd in intervals[1:]:
            prevStart, prevEnd = res[-1]
            if curStart <= prevEnd:
                res[-1] = [prevStart, max(curEnd, prevEnd)]
            else:
                res.append([curStart, curEnd])
        
        return res

        