from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dive(node, level):
            if not node:
                return

            if len(res) <= level:
                res.append(node.val)

            dive(node.right, level + 1)
            dive(node.left, level + 1)

        dive(root, 0)

        return res
