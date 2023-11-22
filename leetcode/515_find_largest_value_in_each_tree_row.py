# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = deque([root])
        res = []
        cur_max = float('-inf')

        while d:

            next_d = deque()
            while d:
                node = d.pop()
                cur_max = max(cur_max, node.val)
                if l := node.left:
                    next_d.append(l)
                if r := node.right:
                    next_d.append(r)
            res.append(cur_max)
            cur_max = float('-inf')
            d = next_d

        return res
