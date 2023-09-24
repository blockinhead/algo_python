from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # на самом деле это не нужно
        if not head or not head.next:
            return head

        res = ListNode(-101, head)
        first = res
        second = res.next

        while second != None:
            if second.next and second.val == second.next.val:
                while second.next and second.val == second.next.val:
                    second = second.next

                first.next = second.next
            else:
                first = first.next

            second = second.next

        return res.next
