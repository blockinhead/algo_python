from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbours = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0),         (1, 0),
                      (-1, -1), (0, -1), (1, -1)]

        def filter_neighbours(i, j):
            def fx(x):
                if x < 0 or x > len(board) - 1:
                    return False
                return True

            def fy(y):
                if y < 0 or y > len(board[0]) - 1:
                    return False
                return True

            return filter(lambda x: fx(x[0] + i) and fy(x[1] + j), neighbours)

        def iterate(i, j):
            # on current iteration all positive is alive, negative or zero is dead
            # if alive cell is going to be dead lets mark it 2
            # if dead cell is going to be alive, lets mark it -1
            # after %2 they become 0 or 1 again

            fn = list(filter_neighbours(i, j))
            n = filter(lambda x: board[x[0] + i][x[1] + j] > 0, filter_neighbours(i, j))
            n = list(n)
            n = len(n)
            if board[i][j] > 0 and (n < 2 or n > 3):
                board[i][j] = 2
            if board[i][j] <= 0 and n == 3:
                board[i][j] = -1

        for i in range(len(board)):
            for j in range(len(board[0])):
                iterate(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] %= 2


b = [[1, 1], [1, 0]]
Solution().gameOfLife(b)
print(b)
