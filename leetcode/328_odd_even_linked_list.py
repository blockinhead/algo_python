# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_dummy = ListNode()
        odd_dummy = ListNode()
        even = even_dummy
        odd = odd_dummy

        node = head
        while node and node.next:
            odd.next = node
            even.next = node.next
            odd = odd.next
            even = even.next
            node = node.next.next

        if node:
            odd.next = node
            odd = odd.next
        odd.next = even_dummy.next
        even.next = None

        return odd_dummy.next
