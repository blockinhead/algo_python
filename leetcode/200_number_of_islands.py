from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dive(i, j):
            if (0 <= i < len(grid)) and (0 <= j < len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = 2
                    for n, m in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        dive(i + n, j + m)


        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dive(i, j)

        return num_islands
