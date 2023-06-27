# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 0
        targetNode = ListNode(0,None)
        current = head
        previous = ListNode(0,head)
        prev = previous

        

        while current:
            listLength += 1
            if listLength == n:
                targetNode = head
                while current.next:
                    current = current.next
                    prev = prev.next 
                    targetNode = targetNode.next
                prev.next = targetNode.next
                return previous.next
            current = current.next  