from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        # все интервалы, которые левее начала нового интервала попадают в ответ без изменений
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        # дальше добавляем в ответ новый интервал
        res.append(newInterval)

        # возможно, интервалы кончились
        if i == len(intervals):
            return res

        # возможно левая граница следующего интервала левее правой границы нашего интервала
        # (на самом деле можно проверить, что она левее левой, тогда можно без минимума, просто присвоить)
        if intervals[i][0] <= newInterval[1]:
            res[-1][0] = min(res[-1][0], intervals[i][0])

        # если мы вставили очень здоровый новый интервал, то он может захватить левые границы старых интервалов,
        # но по услоивю интервалы не должны пересекаться, значит надо смаржить
        while i < len(intervals):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

            else:
                res.append(intervals[i])

            i += 1

        return res


print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(Solution().insert(intervals=[[1, 5]], newInterval=[5, 7]))
print(Solution().insert(intervals=[[1, 5]], newInterval=[6, 7]))
