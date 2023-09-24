from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        d = []
        for _ in range(len(obstacleGrid)):
            d.append([0] * len(obstacleGrid[0]))

        d[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                d[i][0] = d[i - 1][0]
            else:
                break

        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                d[0][i] = d[0][i - 1]
            else:
                break

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]

        return d[-1][-1]
