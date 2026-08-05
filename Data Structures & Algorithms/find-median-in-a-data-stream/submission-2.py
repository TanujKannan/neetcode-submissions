'''
We want to use two heaps:
1. Small
    1. Stores the smaller half of the values. 
    2. We want the largest of the small half.
    3. So it's a max heap
2. Large
    1. Stores the larger half of the values
    2. We want the smallest of the large half
    3. So it's a min heap

Main thing that needs to hold:
1. At any given moment, the two heaps can differ by at most 1 in length.

So if we find that this property is being threatened, then we pop from the top of the longer one
and push it into the shorter one, appropriately.

When we want the median:
1. If one is longer, take the top of that heap.
2. If both are same length, take the mean of their top values.

For any new value:
1. If it's larger than the smallest in large, push it into large.
2. Otherwise, push it into small.
'''
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
        elif len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0])/2.0
        
        