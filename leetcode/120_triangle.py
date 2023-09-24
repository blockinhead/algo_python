from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        d = []
        for i in range(len(triangle)):
            d.append([float('inf') for _ in range(len(triangle[i]))])

        d[0][0] = triangle[0][0]
        for i in range(len(triangle) - 1):
            for j in range(len(triangle[i])):
                d[i + 1][j] = min(d[i + 1][j], triangle[i + 1][j] + d[i][j])
                d[i + 1][j + 1] = min(d[i + 1][j + 1], triangle[i + 1][j + 1] + d[i][j])

            # print(d)

        return min(d[-1])
