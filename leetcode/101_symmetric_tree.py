from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        d1 = deque()
        d1.append(root.left)
        d2 = deque()
        d2.append(root.right)

        while d1 or d2:
            n1 = d1.pop()
            n2 = d2.pop()

            if bool(n1) != bool(n2):
                # print(f'{n1=} {n2=}')
                return False

            if not n1 and not n2:
                continue

            if n1.val != n2.val:
                # print(f'{n1=} {n2=}')
                return False

            d1.append(n1.left)
            d2.append(n2.right)
            d1.append(n1.right)
            d2.append(n2.left)

        return d1 == d2
