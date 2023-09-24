from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        d = deque()
        current_node = root

        while d or current_node:
            if current_node:
                d.append(current_node)
                current_node = current_node.left
            else:
                node = d.pop()
                k -= 1
                if not k:
                    return node.val

                current_node = node.right

# фокус в том, чтобы понять как обходить бст (см 530) и что в результате инфиксного обхода получается отсортированная последовательность
