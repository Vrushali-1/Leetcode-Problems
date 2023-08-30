# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        pathNumber = finalAddition = 0

        if not root:
            return 0

        while root:
            if root.left:
                previous = root.left
                step = 1
                while previous.right and previous.right != root:
                    previous = previous.right
                    step += 1
                
                if not previous.right:
                    pathNumber = pathNumber * 10 + root.val
                    previous.right = root
                    root = root.left
                else:
                    if not previous.left:
                        finalAddition += pathNumber
                    for _ in range(step):
                        pathNumber //= 10
                    root = root.right
                    previous.right = None
            
            else:
                pathNumber = pathNumber * 10 + root.val
                if not root.left and not root.right:
                    finalAddition += pathNumber
                root = root.right
        return finalAddition
        