class Solution:
    def leastInterval(self, tasks, n):
        queue = deque()

        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        cycles = 0

        while maxHeap or queue:
            cycles += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq != 0:
                    queue.append([freq, cycles + n])
                
            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.popleft()[0])
    
        return cycles
        