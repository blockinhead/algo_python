class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0] * n for _ in range(m)]

        for i in range(n):
            d[0][i] = 1

        for j in range(m):
            d[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                d[j][i] = d[j][i - 1] + d[j - 1][i]

        return d[-1][-1]
