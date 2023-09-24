from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def construct(side_len, row, col):
            if side_len == 1:
                return Node(grid[row][col], isLeaf=True)
            # else:

            side_len = side_len // 2
            topLeft=construct(side_len, row, col)
            topRight=construct(side_len, row, col + side_len)
            bottomLeft=construct(side_len, row + side_len, col)
            bottomRight=construct(side_len, row + side_len, col + side_len)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf \
                and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(val=topLeft.val,
                            isLeaf=True)
            else:
                return Node(val=0,
                            isLeaf=False,
                            topLeft=topLeft,
                            topRight=topRight,
                            bottomLeft=bottomLeft,
                            bottomRight=bottomRight)

        return construct(len(grid), 0, 0)
