# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        res = 0
        d = deque()
        if root.left:
            d.append((root.left, 0, 1))  # node, left, 1 step
        if root.right:
            d.append((root.right, 1, 1))  # node, right, 1 step

        while d:
            node, prev_dir, zigzag_length = d.pop()
            res = max(res, zigzag_length)
            if node.left:
                d.append((node.left, 0, zigzag_length + 1 if prev_dir == 1 else 1))
            if node.right:
                d.append((node.right, 1, zigzag_length + 1 if prev_dir == 0 else 1))

        return res
