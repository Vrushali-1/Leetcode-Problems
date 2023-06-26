# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        sentinel = ListNode(0,head)
        prev = sentinel

        while head and head.next:
            if head.val != head.next.val:
                prev = head
                head = head.next
            else:
                while head.next and head and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
                head = head.next

        return sentinel.next