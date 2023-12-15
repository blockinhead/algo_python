class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rz = [0] * len(grid)
        ro = [0] * len(grid)
        for i, row in enumerate(grid):
            rz[i] = sum([1 for v in row if v == 0])
            ro[i] = sum([1 for v in row if v == 1])

        cz = [0] * len(grid[0])
        co = [0] * len(grid[0])
        for i, col in enumerate(zip(*grid)):
            cz[i] = sum([1 for v in col if v == 0])
            co[i] = sum([1 for v in col if v == 1])

        res = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = ro[i] + co[j] - rz[i] - cz[j]

        return res
