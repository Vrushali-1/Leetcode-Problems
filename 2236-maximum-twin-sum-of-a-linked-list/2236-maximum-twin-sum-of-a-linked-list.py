# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        maximumSum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        while prev:
            maximumSum = max(maximumSum,head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return maximumSum