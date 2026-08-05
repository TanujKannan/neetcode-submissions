# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, leftBound, rightBound):
            if not node:
                return True
            
            if node.val <= leftBound or node.val >= rightBound:
                return False
            
            left = validate(node.left, leftBound, node.val)
            right = validate(node.right, node.val, rightBound)

            return left and right
        
        return validate(root, float('-inf'), float('inf'))
        