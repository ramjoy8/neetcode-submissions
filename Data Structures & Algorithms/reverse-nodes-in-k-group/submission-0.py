# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummy = ListNode()

        dummy.next = head
        prev_grp_last = dummy

        while True:

            kth = prev_grp_last

            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            curr = prev_grp_last.next
            next_group = kth.next
            prev = next_group

            while curr != next_group:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            tmp = prev_grp_last.next
            prev_grp_last.next = kth
            prev_grp_last = tmp


