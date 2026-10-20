# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length = length + 1

        ele = length - n + 1


        curr = head
        prev = None
        if ele == 1:
            return curr.next
        while ele>0 and curr:
            if ele == 1:
                next = curr.next
                if prev:
                    prev.next = next
                curr.next = None

            else:
                prev = curr
                curr = curr.next
            ele = ele -1

        
        return head

