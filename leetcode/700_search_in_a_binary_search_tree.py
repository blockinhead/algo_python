# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dive(node):
            if node.val == val:
                return node
            if node.left and val < node.val:
                return dive(node.left)
            if node.right and val > node.val:
                return dive(node.right)
            return None
        return dive(root)
