# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodes = 0
        group = 2

        current = head.next
        con = head
        tail = head.next
        pointer = head.next

        while current:

            while nodes < group and current:
                current = current.next
                nodes += 1
            
            prev = None
            
            if nodes%2 == 0:
                while nodes != 0 and pointer:
                    temp = pointer.next
                    pointer.next = prev
                    prev = pointer
                    pointer = temp
                    nodes -= 1
                con.next = prev
                tail.next = pointer
                con = tail
                tail = pointer
            else:
                while nodes != 0 and pointer:
                    pointer = pointer.next
                    con = con.next
                    nodes -= 1
            tail = pointer
            group += 1

        return head

