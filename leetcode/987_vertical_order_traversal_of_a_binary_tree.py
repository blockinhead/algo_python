# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        c_min, c_max = float('inf'), float('-inf')

        def dive(node, col, row):
            if not node:
                return
            d[col].append((row, node.val))
            nonlocal c_min
            nonlocal c_max
            c_min = min(c_min, col)
            c_max = max(c_max, col)
            dive(node.left, col - 1, row + 1)
            dive(node.right, col + 1, row + 1)

        dive(root, 0, 0)

        res = []
        for i in range(c_min, c_max + 1):
            col = d[i]
            res.append([x[1] for x in sorted(col)])

        return res
