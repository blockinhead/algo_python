from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for _ in range(n):
            first = first.next

        if not first:
            return head.next

        # print(f'{first.val=}. starting the chase')

        while first.next != None:
            first = first.next
            second = second.next
            # print(first.val, second.val)

        # print(second)

        second.next = second.next.next

        # print(head)

        return head
