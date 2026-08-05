class Solution:
    class UnionFind():
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.size = [1]*n
        
        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, a,b):
            root_a = self.find(a)
            root_b = self.find(b)

            if root_a == root_b:
                return False
            
            if self.size[root_a] >= self.size[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            
            return True
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi , yi = points[i]
                xj , yj = points[j] 
                md = abs(xi-xj) + abs(yi-yj)
                edges.append((md, i , j))

        edges.sort()
        cost = 0
        dsu = self.UnionFind(n)
        edges_used = 0

        for md, a,b in edges:
            if dsu.union(a,b):
                cost += md
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return cost