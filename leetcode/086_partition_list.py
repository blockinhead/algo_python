from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d_less = ListNode()
        d_greater = ListNode()

        res = d_less
        tmp = d_greater

        n = head
        while n:
            nn = n.next
            n.next = None
            if n.val < x:
                d_less.next = n
                d_less = d_less.next
            else:
                d_greater.next = n
                d_greater = d_greater.next
            n = nn

        d_less.next = tmp.next

        return res.next
