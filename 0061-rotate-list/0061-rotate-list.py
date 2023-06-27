# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        n = 1   

        # base cases
        if not head:
            return None
        if not head.next:
            return head
        if k == 0:
            return head
        
        while current.next:
            current = current.next 
            n += 1
        k = k % n
        if k == 0:
            return head
            
        current.next = head
        print(n)
        new_tail = head
        for i in range( n - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head if k > 0 else head
