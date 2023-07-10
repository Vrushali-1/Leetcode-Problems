# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = collections.deque([root])
        maximum = []

        while queue:
            currentLevelLength = len(queue)
            currentMax = float('-inf')
            for i in range(currentLevelLength):
                node = queue.popleft()
                currentMax = max(currentMax,node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            maximum.append(currentMax)
        return maximum