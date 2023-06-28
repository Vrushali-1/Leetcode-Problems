# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head.next
        prev = head
        temp = head.next
        tail = head.next

        groupCount = 2
        nodeCount = 0

        if not head or not head.next:
            return head
        
        while current:
        
            while(current and nodeCount < groupCount):
                current = current.next
                nodeCount += 1
            print(nodeCount)
            if(nodeCount%2 ==0):
                before = None
                while(nodeCount!=0):
                    node = temp.next
                    temp.next = before
                    before = temp
                    temp = node
                    nodeCount -= 1
                prev.next = before
                tail.next = temp
                prev = tail
                tail = temp
            else:
                while(nodeCount!=0):
                    temp = temp.next
                    prev = prev.next
                    nodeCount -= 1
                tail= temp

            groupCount += 1

        return head
            

