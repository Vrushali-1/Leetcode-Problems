# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        maximum = float('-inf')
        counter = 1
        maximumLevel = 0

        while queue:
            length = len(queue)
            currentSum = 0

            for i in range(length):
                node = queue.popleft()
                currentSum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if maximum < currentSum:
                maxLevel = counter
                maximum = currentSum
            counter += 1
        return maxLevel