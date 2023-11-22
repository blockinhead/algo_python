# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        max_lev = 0

        d = deque([root, ])
        level = 1

        while d:
            next_level = deque()
            level_val = 0
            while d:
                node = d.pop()
                level_val += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_val > max_val:
                max_val = level_val
                max_lev = level
            level += 1
            d = next_level

        return max_lev
