# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        current = head
        previous = None
        m,n = left,right

        while m>1:
            previous = current
            current = current.next
            m,n=m-1,n-1
        
        tail,con = current,previous

        while n:
            third = current.next
            current.next = previous
            previous = current
            current = third
            n -= 1

        if con:
            con.next = previous
        else:
            head = previous

        tail.next = current
        return head
        