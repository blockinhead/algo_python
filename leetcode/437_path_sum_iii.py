# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dive(node, val_to_target):
            if not node:
                return 0

            res = 1 if node.val == val_to_target else 0
            res += dive(node.left, val_to_target - node.val)
            res += dive(node.right, val_to_target - node.val)
            return res

        if not root:
            return 0
        return dive(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
