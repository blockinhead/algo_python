from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dive(node):
            if not node:
                return

            if node.left:
                dive(node.left)
            if node.right:
                dive(node.right)
            res.append(node.val)

        dive(root)
        return res
