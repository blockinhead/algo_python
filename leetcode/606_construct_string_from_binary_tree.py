# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dive(node):
            if not node.left and node.right:
                return f'{node.val}()({dive(node.right)})'
            if not node.right and node.left:
                return f'{node.val}({dive(node.left)})'
            if node.right and node.left:
                return f'{node.val}({dive(node.left)})({dive(node.right)})'
            if not node.right and not node.left:
                return f'{node.val}'

        return dive(root)
