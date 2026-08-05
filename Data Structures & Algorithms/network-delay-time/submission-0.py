class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*(n+1)
        dist[k] = 0

        graph = defaultdict(list)

        for source, target, cost in times:
            graph[source].append((target, cost))

        pq = [(0, k)]

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > dist[node]:
                continue
            
            for neighbor, distance in graph[node]:
                if cost + distance < dist[neighbor]:
                    dist[neighbor] = cost + distance
                    heapq.heappush(pq, (cost + distance, neighbor))
        
        return -1 if max(dist[1:]) == float('inf') else max(dist[1:])
        