# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        prev = None
        
        dummy = head.next #store second node as it will be new start of the ll

        while head and head.next:

            if prev:
                prev.next = head.next #new element is present hence remove old element as next element [3] and point to new element that is [4]
            prev = head

            temp = head.next.next #code to swap for odd number elements
            head.next.next = head #code to swap for odd number elements
            head.next = temp  #code to swap for odd number elements
            head = temp #code to swap for odd number elements

        return dummy