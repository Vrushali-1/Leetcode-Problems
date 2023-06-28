# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(0,head)
        prev = sentinel
        tail = head
        count = head
        current = head

        nodeCount = 0

        if not head or not head.next:
            return head


        while count:

            while count and nodeCount<k:
                count = count.next
                nodeCount += 1
            before = None
            if nodeCount == k:
                while nodeCount != 0:
                    temp = current.next
                    current.next = before
                    before = current
                    current = temp
                    nodeCount -= 1
                prev.next = before
                tail.next = current
                prev = tail
                tail = current
        return sentinel.next