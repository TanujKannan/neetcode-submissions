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

        def dfs(node, max_so_far):
            if not node:
                return 0
            count = 0
            
            if node.val >= max_so_far:
                max_so_far = node.val
                count += 1
            
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)

            return left + right + count
        
        return dfs(root, float('-inf'))

        