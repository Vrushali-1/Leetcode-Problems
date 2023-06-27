# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev1 = None
        current = l1
        while current:
            temp = current.next
            current.next = prev1
            prev1 = current
            current = temp
       
        prev2 = None
        current = l2
        while current:
            temp = current.next
            current.next = prev2
            prev2 = current
            current = temp

        carry = 0
        answer = ListNode(0,None)
        current = answer

        while prev1 is not None or prev2 is not None or carry != 0:
            first = prev1.val if prev1 else 0
            second = prev2.val if prev2 else 0

            current.next = ListNode((first + second + carry)%10,None)
            carry = (first + second + carry)//10

            current = current.next

            prev1 = prev1.next if prev1 else None
            prev2 = prev2.next if prev2 else None
        
        prev = None
        current = answer.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
