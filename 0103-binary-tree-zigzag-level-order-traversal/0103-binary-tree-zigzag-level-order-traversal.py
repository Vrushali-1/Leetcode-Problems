# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        ans = []
        evenLevel = True
        if not root:
            return []

        while queue:
            current = len(queue)
            currentLevel = collections.deque()
            
            for i in range(current):
                node = queue.popleft()
                if evenLevel:
                    currentLevel.append(node.val)
                else:
                    currentLevel.appendleft(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(currentLevel)
            evenLevel = not evenLevel
        return ans
                    
        