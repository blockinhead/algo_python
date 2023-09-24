class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ma = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    ma = 1

        # for l in matrix:
        # print(l)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (d := matrix[i - 1][j - 1]) and (l := matrix[i][j - 1]) and (u := matrix[i - 1][j]) and matrix[i][j]:
                    # print(f'{i} {j} {d} {l} {u}')
                    t = min(d, l, u)
                    # print(f'{ma=}')
                    matrix[i][j] = t + 1
                    ma = max(ma, t + 1)

        # for l in matrix:
        # print(l)

        return ma * ma

# у квадрата 2х2, состоящего из единичек, в правй нижний угол можно записать 2.
# тогда у квадрата 3х3 снаружи правого нижнего угла будет уголок из двоек. тогда запишем в угол 3
