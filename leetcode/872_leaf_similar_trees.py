# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs = deque()
        d = deque()
        d.append(root1)

        while d:
            node = d.pop()
            if not node.left and not node.right:
                leafs.append(node.val)
                continue
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)

        d.append(root2)
        while d:
            node = d.pop()
            if not node.left and not node.right:
                if not leafs:
                    return False
                if node.val != leafs.pop():
                    return False

            if node.right:
                d.append(node.right)
            if node.left:
                d.append(node.left)

        if leafs:
            return False

        return True
