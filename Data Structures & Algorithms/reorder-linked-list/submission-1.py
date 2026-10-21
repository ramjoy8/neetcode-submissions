# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        mid = head
        fast = head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        prev = None
        curr = mid.next
        mid.next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        reverse = prev
        start = head

        while reverse:
            reverse_next = reverse.next
            start_next = start.next

            start.next = reverse
            reverse.next = start_next

            reverse = reverse_next
            start = start_next

