"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        

        if not head:
            return head
        current = head

        while current:
            newNode = Node(current.val,None,None)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next
        
        current = head

        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next
        
        current = head
        newHead = current.next
        newList = current.next

        while current:
            current.next = newList.next
            newList.next = newList.next.next if newList.next else None
            newList = newList.next
            current = current.next
        
        return newHead

