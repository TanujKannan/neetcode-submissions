class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, destination, cost in flights:
            graph[source].append((cost, destination))
        
        min_stops = [float('inf')]*n

        pq = [(0, src, 0)]

        while pq:
            cost, node, stops_used = heapq.heappop(pq)

            if node == dst:
                return cost
            
            if stops_used == k + 1:
                continue
            
            if stops_used >= min_stops[node]:
                continue
            
            min_stops[node] = stops_used

            for nextCost, neighbor in graph[node]:
                heapq.heappush(pq, (nextCost + cost, neighbor, stops_used + 1))
        
        return -1
        