from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # сортируем отрезки по левому краю
        res = [intervals[0]]

        for x, y in intervals:
            # если левый конец текущего отрезка лежит внутри верхнего среди результатов отрезка, то обновляем результат правым концом
            if x <= res[-1][1]:
                res[-1][1] = max(res[-1][1], y)
            # отрезки отсортированы. новый отрезок вышел из интервала, который сверху результатов, значит начинается новый интервал
            else:
                res.append([x, y])

        return res


print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
