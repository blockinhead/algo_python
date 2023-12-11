class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res = 0
        cols = len(matrix[0])
        cons_ones = [0] * cols  # здусь будет сколько единичек подряд накопилось в и-ой колонке на данный шаг

        for row in matrix:
            for i, v in enumerate(row):
                if v == 0:
                    cons_ones[i] = 0
                else:
                    cons_ones[i] += 1

            for i, v in enumerate(
                    sorted(cons_ones)):  # так как количество единичек отсортировано от меньшего к большему, можно построить прямоугольник
                if v == 0:
                    continue
                res = max(res, v * (cols - i))

        return res
