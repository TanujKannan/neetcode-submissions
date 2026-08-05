class Solution:
    '''
    At each step, choose two heaviest. x and y
    If x == y, both destroyed.
    If x < y, just push back y - x
    Do this while len(heap) > 1
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, x - y)


        return -maxHeap[0] if maxHeap else 0

        

        