from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = deque()

        node = root
        while node:
            self.q.append(node)
            node = node.left

    def next(self) -> int:
        node = self.q.pop()
        val = node.val

        node = node.right
        while node:
            self.q.append(node)
            node = node.left

        return val

    def hasNext(self) -> bool:
        return bool(self.q)
