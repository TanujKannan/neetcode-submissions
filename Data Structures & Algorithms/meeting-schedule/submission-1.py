"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x:x.start)
        prevStart, prevEnd = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            curStart, curEnd = interval.start, interval.end
            if prevEnd > curStart:
                return False
            else:
                prevEnd = curEnd
        return True
