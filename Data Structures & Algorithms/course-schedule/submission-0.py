class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0]*numCourses

        for a , b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        queue = deque([])

        for i , indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        processed = 0
        while queue:
            course = queue.popleft()
            processed += 1

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return processed == numCourses        