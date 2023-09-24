from pprint import pprint


def setZeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zfr = 0 in matrix[0]
    zfc = False
    for row in matrix:
        if 0 == row[0]:
            zfc = True
            break

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            matrix[i] = [0] * len(matrix[0])

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    if zfc:
        for i in range(1, len(matrix)):
            matrix[i][0] = 0

    if zfr:
        matrix[0] = [0] * len(matrix[0])


m = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
pprint(m)
setZeroes(None, m)
pprint(m)
