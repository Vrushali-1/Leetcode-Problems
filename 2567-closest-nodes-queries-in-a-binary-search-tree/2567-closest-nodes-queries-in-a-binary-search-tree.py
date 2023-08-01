# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            array.append(root.val)
            inorder(root.right)
        

        def binarySearch(array, target):
            left = 0
            right = len(array)
            while left < right:
                mid = (left + right) // 2
                if array[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left
        
        array = []
        inorder(root)
        answer = []
        for query in queries:
            index = binarySearch(array,query)

            if 0 <= index < len(array) and array[index] == query:
                answer.append([query,query])
            else:
                temp = [-1,-1]
                if index > 0:
                    temp[0] = array[index - 1]
                if index < len(array):
                    temp[1] = array[index]
                answer.append(temp)
        return answer
