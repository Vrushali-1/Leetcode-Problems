# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        answer = ListNode(0,None)
        small = answer

        large = ListNode(0,head)
        prev = large

        while head:
            if head.val < x:
                prev.next = head.next
                small.next = head
                head = head.next
                small = small.next
            else:
                prev = prev.next
                head = head.next
        small.next = large.next
        return answer.next
                
