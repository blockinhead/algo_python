from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        max_path_len = m * n

        d = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    d.append((i, j))
                else:
                    mat[i][j] = max_path_len

        while d:
            i, j = d.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + dx, j + dy
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    continue
                if mat[ii][jj] > mat[i][j] + 1:
                    mat[ii][jj] = mat[i][j] + 1
                    d.append((ii, jj))

        return mat


print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
