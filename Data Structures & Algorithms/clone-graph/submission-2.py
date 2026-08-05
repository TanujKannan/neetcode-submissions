"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        originalToCopy = {}
        copy = Node(node.val, [])
        originalToCopy[node] = copy

        queue = deque([node])

        while queue:
            popped_node = queue.popleft()
            copy_node = originalToCopy[popped_node]

            for neighbor in popped_node.neighbors:
                if neighbor not in originalToCopy:
                    originalToCopy[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                copy_node.neighbors.append(originalToCopy[neighbor])
        
        return originalToCopy[node]
                    