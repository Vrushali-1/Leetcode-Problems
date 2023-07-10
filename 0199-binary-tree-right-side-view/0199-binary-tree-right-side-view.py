# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        answer = []

        if not root:
            return []

        while queue:
            currentLevelLength = len(queue)
            answer.append(queue[-1].val)

            for i in range(currentLevelLength):
                temp = queue.popleft()
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
        return answer