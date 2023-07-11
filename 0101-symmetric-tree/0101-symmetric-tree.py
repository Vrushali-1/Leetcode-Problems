# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(p,q):
            if not p and not q:
                return True
        
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            left = isMirror(p.right,q.left)
            right = isMirror(p.left,q.right)

            return left and right
        return isMirror(root,root)
        
