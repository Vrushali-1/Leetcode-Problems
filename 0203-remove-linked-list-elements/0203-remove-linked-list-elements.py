# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0,head)
        previous  = sentinel

        while head:
            if head.val == val:
                previous.next =  head.next
                head = head.next
            else:
                previous = head
                head = head.next
        return sentinel.next
