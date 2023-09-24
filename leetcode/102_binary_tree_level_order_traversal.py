from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        depth = 0

        if not root:
            return []

        def dive(node=root, level=0):
            if not node:
                return

            dive(node.left, level + 1)

            levels[level].append(node.val)
            nonlocal depth
            depth = max(depth, level)

            dive(node.right, level + 1)

        dive()

        return [levels[i] for i in range(depth + 1)]
