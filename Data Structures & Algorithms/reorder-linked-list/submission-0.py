# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        reverse_list = prev
        curr = head

        while reverse_list:
            curr_next = curr.next
            reverse_list_next = reverse_list.next

            curr.next = reverse_list
            reverse_list.next = curr_next

            curr = curr_next
            reverse_list = reverse_list_next



        


