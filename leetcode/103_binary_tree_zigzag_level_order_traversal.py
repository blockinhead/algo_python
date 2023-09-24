from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()

        q.append(root)
        res = [[root.val]]

        while q:
            next_q = deque()
            next_level_vals = []

            while q:
                node = q.pop()

                if len(res) % 2 != 0:
                    if node.right:
                        next_q.append(node.right)
                        next_level_vals.append(node.right.val)
                    if node.left:
                        next_q.append(node.left)
                        next_level_vals.append(node.left.val)
                else:
                    if node.left:
                        next_q.append(node.left)
                        next_level_vals.append(node.left.val)
                    if node.right:
                        next_q.append(node.right)
                        next_level_vals.append(node.right.val)

            q = next_q
            res.append(next_level_vals)

        res.pop()  # после последнего внутреннего вайла в ответе будет лишний пустой списко слева
        return res
