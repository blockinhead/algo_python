from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        d = deque()
        current_node = root

        prev_val = None
        min_dif = float('inf')

        while d or current_node:
            if current_node:
                d.append(current_node)
                current_node = current_node.left
            else:
                node = d.pop()
                print(node.val)

                if prev_val is None:
                    prev_val = node.val
                else:
                    min_dif = min(min_dif, node.val - prev_val)
                    prev_val = node.val

                current_node = node.right

        return min_dif

# same as 530
