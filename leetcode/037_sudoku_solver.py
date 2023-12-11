from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        squares = {(i, j): set() for i in range(3) for j in range(3)}

        def valid(col, row, val):
            if val in rows[row] or val in cols[col] or val in squares[(col // 3, row // 3)]:
                return False
            rows[row].add(val)
            cols[col].add(val)
            squares[(col // 3, row // 3)].add(val)
            return True

        def invalid(col, row, val):
            rows[row].remove(val)
            cols[col].remove(val)
            squares[(col // 3, row // 3)].remove(val)

        for row, r in enumerate(board):
            for col, v in enumerate(r):
                rows[row].add(v)
                cols[col].add(v)
                squares[(col // 3, row // 3)].add(v)

        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row + 1, 0)

            if board[row][col] != '.':
                return solve(row, col + 1)

            for v in range(1, 10):
                v = str(v)
                if valid(col, row, v):
                    board[row][col] = v
                    if solve(row, col + 1):
                        return True
                    else:
                        board[row][col] = '.'
                        invalid(col, row, v)

            return False

        solve(0, 0)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
from pprint import pprint
pprint(board)
