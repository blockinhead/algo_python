class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_next_val(self, li):
        if not li:
            return False, 0
        return li.next, li.val

    def add_vals(self, val1, val2):
        s = val1 + val2
        return s % 10, int(s // 10)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode(0)
        current = res
        next_l1, next_l2 = l1, l2
        rem = 0

        while True:
            next_l1, val1 = self.get_next_val(next_l1)
            next_l2, val2 = self.get_next_val(next_l2)
            s, rem = self.add_vals(val1, val2 + rem)
            current.next = ListNode(s)
            current = current.next
            if not next_l1 and not next_l2:
                if rem:
                    current.next = ListNode(rem)
                break

        return res.next
