# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isBalanced(root):
            if not root:
                return True,0
            
            leftBalanced,leftheight = isBalanced(root.left)

            if not leftBalanced: return False,0

            rightBalanced, rightheight = isBalanced(root.right)

            if not rightBalanced: return False,0

            return abs(leftheight - rightheight) <= 1, 1 + max(leftheight,rightheight)

        return isBalanced(root)[0]
