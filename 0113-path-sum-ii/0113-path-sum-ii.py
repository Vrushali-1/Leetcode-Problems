# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def helper(root,currentPath,remainingSum):
            if not root: return 

            currentPath.append(root.val)

            if not root.left and not root.right and remainingSum == root.val:
                answer.append(list(currentPath))
            else:
                helper(root.left,currentPath, remainingSum - root.val)
                helper(root.right,currentPath,remainingSum - root.val)

            currentPath.pop()       
        
        helper(root,[],targetSum)
        return answer