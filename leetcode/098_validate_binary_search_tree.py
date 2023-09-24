from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        d = deque()
        current_node = root

        prev_val = None

        while d or current_node:
            if current_node:
                d.append(current_node)
                current_node = current_node.left
            else:
                node = d.pop()
                # print(node.val)

                if prev_val is None:
                    prev_val = node.val
                else:
                    # print(prev_val, node.val)
                    if prev_val >= node.val:
                        return False
                    prev_val = node.val

                current_node = node.right

        return True

# same as 530 and 783
