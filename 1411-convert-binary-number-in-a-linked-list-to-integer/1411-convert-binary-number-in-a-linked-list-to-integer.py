# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        listlength = 0
        current = head
        addition = 0
        while current:
            current = current.next
            listlength += 1
        while head:
            if head.val == 1:
                addition += 2**(listlength-1)
            listlength -= 1
            head = head.next
        return addition
