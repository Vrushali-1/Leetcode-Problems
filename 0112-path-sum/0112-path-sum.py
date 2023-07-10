# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def getSum(root: Optional[TreeNode],current: int) -> bool:
            if root is None:
                return False
            
            if not root.left and not root.right:
                return (current + root.val) == targetSum

            current += root.val
            left = getSum(root.left,current)
            right = getSum(root.right,current)

            return left or right

        return getSum(root,0) 