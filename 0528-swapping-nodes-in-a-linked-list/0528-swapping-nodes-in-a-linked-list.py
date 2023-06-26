# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        frontNode = ListNode(0,None)
        endNode = ListNode(0,None)
        currentNode = head

        while currentNode:
            length += 1
            if length == k:
                frontNode = currentNode
                endNode = head
                while currentNode.next:
                    currentNode = currentNode.next
                    endNode = endNode.next
                frontNode.val,endNode.val = endNode.val,frontNode.val
                return head
            currentNode = currentNode.next