# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = float('inf')
        current = []

        def inorder(root):
            if not root:
               return
            
            left = inorder(root.left)
            current.append(root.val)
            right = inorder(root.right)

        inorder(root)

        for i in range(1,len(current)):
            answer = min(answer, current[i] - current[i-1])
        
        return answer




