from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        def k_b(p1, p2):
            if p1[0] == p2[0]:
                return float('inf'), p1[0]

            k = (p2[1] - p1[1]) / (p2[0] - p1[0])
            return k, p2[1] - p2[0] * k

        slopes = defaultdict(set)
        res = 0

        for i in range(len(points) - 1):
            for j in range(i, len(points)):
                k, b = k_b(points[i], points[j])
                slopes[(k, b)].add((points[i][0], points[i][1]))
                slopes[(k, b)].add((points[j][0], points[j][1]))

                res = max(len(slopes[(k, b)]), res)

        return res

# для каждой точки считаем k и b (y = kx + b) через все следующие точки
    
# можно было бы для каждой точки считать только угол со всеми следующими точками. брать максимум.
# для следующей точки тоже считать угол со всеми следующими, брать максимум, сравнивать максимумы.
# то есть словарь был бы не по к и б, только по к, и словарь был бы внутри внешнего фора
# так было бы быстрее
