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

        curr = head
        if not head:
            return None

        while curr:
            copy = Node(curr.val)
            copy.next = curr.next 
            curr.next = copy
            curr = copy.next

        curr = head
        copy_head = curr.next
        while curr:
            random = curr.random
            if random:
                curr.next.random = random.next
            curr = curr.next.next

        curr = head

        while curr:
            copy = curr.next
            curr.next = copy.next
            if curr.next:
                copy.next = curr.next.next
            curr = curr.next
        return copy_head




        