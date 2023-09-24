from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'<{self.val} {self.next}>'


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        current_group = dummy

        while True:
            node = current_group
            counter = k
            while node and counter:
                node = node.next
                counter -= 1
            if not node:
                return dummy.next

            next_group = node.next

            new_next = next_group
            current = current_group.next
            while current != next_group:
                cache = current.next
                current.next = new_next
                new_next = current
                current = cache

            tmp = current_group.next
            current_group.next = new_next
            current_group = tmp


print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), k=2))
