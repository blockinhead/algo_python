from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        d = deque()
        node = root
        while True:
            if node:
                d.append(node)
                node = node.left
            else:
                if not d:
                    break

                node = d.pop()
                res.append(node.val)
                node = node.right

        return res


class RecurentSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dive(node):
            if not node:
                return
            dive(node.left)
            res.append(node.val)
            dive(node.right)

        dive(root)
        return res
