class Solution:
    class UnionFind():
        def __init__(self, n):
            self.parent = [i for i in range(n+1)]
            self.size = [1]*(n+1)
        
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = self.UnionFind(len(edges))
        res = []

        for a, b in edges:
            if not dsu.union(a,b):
                res = [a,b]
        
        return res
        