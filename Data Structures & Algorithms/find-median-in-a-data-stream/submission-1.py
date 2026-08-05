class MedianFinder:

    def __init__(self):
        '''
        We want the small heap to be a max heap so that we can get the largest of the smaller half
        We want the large heap to be a min heap so that we can get the smallest of the larger half
        '''
        self.small = [] #max heap
        self.large = [] #min heap
        

    def addNum(self, num: int) -> None:
        '''
        For the first element, add it to the large heap
        For every element after, we need to decide which heap to put it into.
        If it's larger than the smallest in our large heap, then put it into the large heap
        Otherwise, if it's smaller than the smallest in our large heap, put it into the small heap
        If at any moment, the heap sizes differ by 1, then take the top from the longer one and push into the shorter one
        '''
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        '''
        If both heaps have the same size, then return the average of max of small and min of large
        Otherwise, get the top from whichever is larger.
        '''
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0])/2.0
        
        