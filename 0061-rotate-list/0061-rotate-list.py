# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        n = 1   
         
        #base case
        if not head:
            return None
        if not head.next:
            return head

        while current.next:
            current = current.next 
            n += 1
        k = k % n #actually how many times to rotate

        # base cases
        if k == 0:
            return head
      
            
        current.next = head #connect current to current head to make a ring

        new_tail = head #again start new tail from previous head
        for i in range( n - k - 1): #new tail will be n-k-1th node
            new_tail = new_tail.next
        new_head = new_tail.next #assign new head

        new_tail.next = None #break the ring

        return new_head 
