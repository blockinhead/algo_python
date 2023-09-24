from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)

        counter = 1
        current_right = points[0][1]
        i = 1
        while i < len(points):
            if points[i][0] > current_right:
                counter += 1
                current_right = points[i][1]
            i += 1

        return counter

# сортируем шарики по правому краю
# берём первый шарик. первой стрелой можно будет пробить все шарики, левая граница которых лежит не дальше, чем правая граница первого шарика
# как только мы увидим шарик, левая граница которого лежит дальше чем заканчивается первый шарик, нам нужна будет новая стрела
print(Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
