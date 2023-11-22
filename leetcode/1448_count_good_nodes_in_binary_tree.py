# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        d = deque()
        d.append((root, root.val))
        res = 1

        while d:
            node, max_ = d.pop()

            if node.left:
                res += 1 if node.left.val >= max_ else 0
                d.append((node.left, max(max_, node.left.val)))
            if node.right:
                res += 1 if node.right.val >= max_ else 0
                d.append((node.right, max(max_, node.right.val)))

        return res
