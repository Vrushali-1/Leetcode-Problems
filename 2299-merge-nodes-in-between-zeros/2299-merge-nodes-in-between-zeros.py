# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        start = head
        current = head

        while current:
            addition = 0
            while current.val != 0:     
                addition += current.val
                current = current.next
            start.val = addition
            current = current.next
            start.next = current
            start = current
        return head
            