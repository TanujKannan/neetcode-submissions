# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            isBalancedLeft, heightLeft = dfs(node.left)
            isBalancedRight, heightRight = dfs(node.right)

            if (isBalancedLeft and isBalancedRight) and (abs(heightLeft - heightRight)) <= 1:
                return [True, max(heightLeft, heightRight) + 1]
            else:
                return [False, -1]
        isBalanced, height = dfs(root)
        return isBalanced
            

        