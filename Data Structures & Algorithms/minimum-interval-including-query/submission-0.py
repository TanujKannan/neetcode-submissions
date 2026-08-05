
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])

        res = {}
        i = 0
        minHeap = []

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l , r = intervals[i][0], intervals[i][1]
                heapq.heappush(minHeap, (r - l + 1, r))
                i+=1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[query] = minHeap[0][0]
            else:
                res[query] = -1
        
        return [res[q] for q in queries]

        