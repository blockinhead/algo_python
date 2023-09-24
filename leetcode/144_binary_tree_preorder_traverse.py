from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        '''

        def dive(node):
            if not node:
                return

            res.append(node.val)
            if node.left:
                dive(node.left)
            if node.right:
                dive(node.right)

        dive(root)      
        return res
        '''

        d = deque()
        d.append(root)

        while d:
            n = d.pop()

            if not n:
                break

            res.append(n.val)
            # то, что добавляешь раньше, выйдет из деки позже. нам надо сначала сходить налево
            if n.right:
                d.append(n.right)
            if n.left:
                d.append(n.left)

        return res
