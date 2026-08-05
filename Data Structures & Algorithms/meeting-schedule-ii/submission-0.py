"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
'''
Ideally want meetings with earliest end time to run first.
Always pop the meeting with the earliest end time.
intervals = [(0,40),(5,10),(15,20)]
Sort by end time
(5 10) (15 20) (0 40)
(5 10) (15 20) can use the same room
Need another room for (0 40). Why?
Collides with both (5 10) and (15 20) because it's start time is before
theirs and end time is after.
(0 9) would not collide.

Say only two meetings. How do we know if collision? Sorted by end time.
(a b) (c d)

If c<a and d>b, then they cannot use the same room. But d>b guaranteed.
So collision if c < a.

Say we have a heap that always pops the meeting with the earliest end time.
We need to compare it with something to decide if they can use the same room or not.

Maybe pop twice to get two meetings. If there's no conflict, continue as is.
If there's a conflict, push the second one back.

So len(heap) represents how many meeting rooms we had?

heap pops (5 10) and (15 20). No collision, so do nothing. Heap only has (0 40)
Pop (0 40), but nothing to compare with?

Sort by start times?
[(0 40), (5 10), (15 20)]

Heap represents the active meetings.
So make heap store only end times.
Then for every meeting, compare the start time with the top of the heap.
If it's before, then it cannot use the same room. Start that meeting, push into heap.
If it's after, then it can just wait and use the same room. So do nothing?
'''

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []

        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            elif interval.start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
        
        return len(heap)


        