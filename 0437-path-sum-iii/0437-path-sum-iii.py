# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def helper(root, currentSum):
            nonlocal count
            nonlocal counter
            if not root: return 0

            currentSum += root.val

            count += counter[currentSum - targetSum]

            counter[currentSum] += 1

            helper(root.left,currentSum)
            helper(root.right,currentSum)

            counter[currentSum] -= 1
        
        counter = collections.Counter()
        counter[0] = 1
        count = 0
        
        helper(root, 0)
        return count