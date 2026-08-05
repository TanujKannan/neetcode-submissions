"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        storePairs = []

        for interval in intervals:
            start, end = interval.start, interval.end
            storePairs.append((start, 1))
            storePairs.append((end , -1))

        storePairs.sort()

        max_rooms_needed = 0
        cur_rooms = 0

        for event, flag in storePairs:
            cur_rooms += flag
            if cur_rooms > max_rooms_needed:
                max_rooms_needed = cur_rooms
        
        return max_rooms_needed

