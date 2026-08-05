class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0]*numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        queue = deque([])
        ordering = []

        for i , indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            ordering.append(course)

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(ordering) == numCourses:
            return ordering
        else:
            return []
        