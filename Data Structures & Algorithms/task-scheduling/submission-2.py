class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        maxHeap = [-count for count in counter.values()]

        cycles = 0
        queue = deque([])
        heapq.heapify(maxHeap)

        #As long there's tasks waiting/schedulable, cycles go up
        while maxHeap or queue:
            cycles += 1

            '''
            Get the task with highest frequency that
            is not in cooldown.

            Run it and put it into cooldown
            '''
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                #Decrement it's frequency since we used it
                #Since it's negative, we increment instead.
                freq += 1
                
                #If we haven't used it up
                if freq != 0:
                    #Put it into the queue with cooldown
                    queue.append((freq, cycles + n))
            
            #Check if a task is done with cooldown
            if queue:
                if queue[0][1] == cycles:
                    heapq.heappush(maxHeap, queue.popleft()[0])
        return cycles

        