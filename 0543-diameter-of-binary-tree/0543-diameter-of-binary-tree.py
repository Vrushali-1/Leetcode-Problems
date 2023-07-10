# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def getPath(node):
            
            if not node:
                return 0
            
            nonlocal diameter
            
            left = getPath(node.left)
            right = getPath(node.right)
            
            diameter = max(diameter,left+right)
            
            return max(left,right) + 1
        
        getPath(root)
        
        return diameter
            
        