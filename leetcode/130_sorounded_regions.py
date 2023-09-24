from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dive(i, j):
            sorounded = True
            if (0 <= i < len(board)) and (0 <= j < len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = 0
                    for n, m in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        sorounded = sorounded and dive(i + n, j + m)
                return sorounded
            else:
                return False

        def fill(i, j, val):
            if (0 <= i < len(board)) and (0 <= j < len(board[0])):
                if board[i][j] == 0:
                    board[i][j] = val
                    for n, m in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        fill(i + n, j + m, val)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    sorounded = dive(i, j)
                    # print(i, j, sorounded)
                    if sorounded:
                        fill(i, j, 'X')
                    else:
                        fill(i, j, 'O')
