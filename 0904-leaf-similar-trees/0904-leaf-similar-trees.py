# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root):
            result = []
            if root:
                if not root.left and not root.right:
                    result.append(root.val)
                result.extend(dfs(root.left))
                result.extend(dfs(root.right))
            return result
        
        return dfs(root1) == dfs(root2)