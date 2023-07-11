# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        answer = []

        if not root:
            return []

        while queue:
            length = len(queue)
            current = []

            for i in range(length):
                node = queue.popleft()
                if node: current.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            answer.append(current)
        return answer