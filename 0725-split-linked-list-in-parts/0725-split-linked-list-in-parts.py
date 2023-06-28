# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        sentinel = ListNode(0,head)
        n = 0
        answer = []
        while current:
            n += 1
            current  = current.next
        
        minimumNodes = n//k
        remainingGroups = n%k
        print(n,remainingGroups,minimumNodes)
        for i in range(k):
            current = newHead = ListNode(0,None)
            count = 0
            if(i<remainingGroups):
                while (count < (minimumNodes + 1) and head):
                    current.next = head
                    current = head
                    head = head.next
                    current.next = None
                    count += 1
            else:
                while (count < minimumNodes and head):
                    current.next = head
                    current = head
                    head = head.next
                    current.next = None
                    count += 1
            answer.append(newHead.next)
        return answer
            

