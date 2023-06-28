# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None # break the first half of the list

        previous = None

        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        
        newList = head

        while previous:
            temp = newList.next
            temp2 = previous.next
            newList.next = previous
            previous.next = temp if temp else previous.next
            newList = previous.next
            previous = temp2 if temp else None
        return head


        
