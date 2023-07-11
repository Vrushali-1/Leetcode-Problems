# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        number = 0 #path number
        answer = 0 #addition 

        while root:

            if root.left:

                previous = root.left
                step = 1
                while previous.right and previous.right is not root:
                    previous = previous.right
                    step += 1
                
                if not previous.right:
                    previous.right = root
                    number = number * 10 + root.val
                    root = root.left
                else:
                    if not previous.left:
                        answer += number
                    for i in range(step):
                        number //= 10
                    previous.right = None
                    root = root.right
            
            else:
                number = number * 10 + root.val
                if not root.right:
                    answer += number
                root = root.right
        return answer
             

