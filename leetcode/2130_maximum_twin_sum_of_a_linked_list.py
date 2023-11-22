# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        d = deque()

        while fast:
            d.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = float('-inf')
        while d:
            res = max(res, d.pop() + slow.val)
            slow = slow.next

        return res
