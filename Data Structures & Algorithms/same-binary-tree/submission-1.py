# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a , b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False
            
            left = dfs(a.left, b.left)
            right = dfs(a.right, b.right)

            return left and right
        
        return dfs(p, q)
        