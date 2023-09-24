from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val

        d = deque()
        res = 0

        d.append((root, []))

        while d:
            node, vals = d.pop()
            # print(f'{node.val=} {vals=}')

            if not node.left and not node.right:
                res += int(''.join(vals)) * 10 + node.val
                continue

            if node.left:
                d.append((node.left, vals + [str(node.val)]))

            if node.right:
                d.append((node.right, vals + [str(node.val)]))

        return res


# обходим дерево, собирая по дороге цифры для числа. когда листьев нет, собираем число
