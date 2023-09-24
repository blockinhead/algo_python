from math import ceil
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dive(start, end):
            if end < start:
                return None
            mid = start + ceil((end - start) / 2)
            # print(f'{start=} {mid=} {end=}')
            r = TreeNode(nums[mid])
            r.left = dive(start, mid - 1)
            r.right = dive(mid + 1, end)
            return r

        return dive(0, len(nums) - 1)
