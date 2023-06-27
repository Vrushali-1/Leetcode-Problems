# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0,None)
        current = answer
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            current.next = ListNode((l1val+l2val+carry)%10,None)
            carry = (l1val + l2val + carry)//10

            
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return answer.next