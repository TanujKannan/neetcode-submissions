'''
Don't want to push all points.
minHeap works properly here.
Maybe push the first k points
After that, for any new point, compare to the current smallest?
If it's smaller then push it. Otherwise dont.
Heap should maintain only k points at any given moment
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = -(x*x + y*y)

            if len(heap) < k:
                heapq.heappush(heap, (distance, x, y))
            
            else:
                if distance > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (distance, x, y))
    
        return [[x,y] for _, x,y in heap]


        