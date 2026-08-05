class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, destination, cost in flights:
            graph[source].append((cost, destination))
        
        min_stops = [float('inf')]*n

        #(cost, node, stops_used)
        heap = [(0, src, 0)]

        while heap:
            cost, node, stops_used = heapq.heappop(heap)

            if node == dst:
                return cost
            
            #If we have used more than the allowed stops, must ignore this route
            if stops_used == k + 1:
                continue
            
            #If we have already found a way to get here that's cheaper and uses fewer stops, ignore this path
            if min_stops[node] <= stops_used:
                continue
            
            #Update min_stops for this node
            min_stops[node] = stops_used

            #Go through neighbors and push into heap
            for nextCost, neighbor in graph[node]:
                heapq.heappush(heap, (cost + nextCost, neighbor, stops_used + 1))
        
        return -1
        