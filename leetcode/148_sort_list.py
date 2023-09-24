from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(node1, node2):
            dummy = ListNode(0)

            current = dummy
            while node1 and node2:
                if node1.val < node2.val:
                    current.next = node1
                    node1 = node1.next
                else:
                    current.next = node2
                    node2 = node2.next

                current = current.next

            if node1:
                current.next = node1
            if node2:
                current.next = node2

            return dummy.next

        def merge_sort(node):
            if not node or not node.next:
                return node

            slow = node
            fast = node
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None

            return merge(merge_sort(node), merge_sort(slow))

        return merge_sort(head)
