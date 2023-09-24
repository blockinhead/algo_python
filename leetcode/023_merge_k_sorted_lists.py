from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def get_not_none():
            return [n for n in lists if n]

        def get_min(l):
            return min(l, key=lambda x: x.val)

        def iterate_node(node):
            for i, n in enumerate(lists):
                if n == node:
                    lists[i] = node.next
                    break

        res = ListNode()
        current = res
        while nodes := get_not_none():
            current.next = get_min(nodes)
            current = current.next
            iterate_node(current)

        return res.next
