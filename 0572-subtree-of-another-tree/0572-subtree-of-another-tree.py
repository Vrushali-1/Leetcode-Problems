# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):

            if not node: #if given root is empty means no tree & according to constraints subroot will always be nonempty hence return False
               return False
            elif isIdentical(node,subRoot):
                return True

             #if not at current root check in left or right children
            return dfs(node.left) or dfs(node.right)
        
        def isIdentical(root1,root2):
            # If any one Node is Empty, both should be Empty
            if not root1 or not root2:
                return not root1 and not root2
        
            return (root1.val == root2.val and
                    isIdentical(root1.left, root2.left) and
                    isIdentical(root1.right, root2.right))
        
        return dfs(root)
        
        