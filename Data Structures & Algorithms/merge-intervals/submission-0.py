'''
intervals = [[1,3],[1,5],[6,7]]

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = []
        res.append(intervals[0])

        for curStart, curEnd in intervals[1:]:
            prevStart, prevEnd = res[-1]
            if prevEnd >= curStart:
                res[-1] = ([prevStart, max(curEnd, prevEnd)])
            else:
                res.append([curStart, curEnd])
        
        return res



        