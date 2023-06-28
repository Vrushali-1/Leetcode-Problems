# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenHead = even = ListNode(0,None)
        current = head
        prev = None
        n = 0

        if not head or not head.next:
            return head

        while current:
            n += 1

            if (n%2) != 0:
                prev = current
                current = current.next
                
            else:
                even.next = current
                even = current
                current = current.next
                prev.next = current
                even.next = None
        prev.next = evenHead.next if evenHead else None
        return head