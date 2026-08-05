# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, max_on_path):
            if not node:
                return 0
            
            count = 0
            if node.val >= max_on_path:
                max_on_path = node.val
                count = 1
            
            left = dfs(node.left, max_on_path)
            right = dfs(node.right, max_on_path)
        
            return left + right + count
        
        return dfs(root, root.val)

        