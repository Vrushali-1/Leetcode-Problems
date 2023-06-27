# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        print('slow: ',slow.val,' fast: ',fast.val)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        temp = head
        temp2 = prev
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

