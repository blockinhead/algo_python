from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        node = head
        left_end = None  # здесь - последняя нода левой части
        for _ in range(left - 1):
            left_end = node
            node = node.next
        rev_start = node  # здесь - начало середины

        prev = None
        for _ in range(right - left + 1):
            prev = node
            node = node.next
        tail = node  # здесь начало правой части
        prev.next = None  # здесь конец середины. тут отрезаем середину от левой части

        # N    current -> nextnode
        # a    b    ->    c
        # a <- b          c
        #      b          c -> d
        #      a          b    c
        # реверсим середину. прям на месте разворачиваем нексты.
        # если просто реверсить, то некстом б был бы нон, но тут можно сразу прекрепить к нему хвост
        new_next = tail
        current = rev_start
        while current:
            cache = current.next
            current.next = new_next
            new_next = current
            current = cache

        # если голова была, то прикрепляем к ней развернутую середину
        if left_end:
            left_end.next = new_next
            return head

        else:
            return new_next
