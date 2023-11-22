class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k: k[0])
        last = intervals[0][1]
        remove = 0

        for i in intervals[1:]:
            if last <= i[0]:  # новый интервал не пересекается с предыдущим, двигаем границу
                last = i[1]
                continue

            # новый интервал пересекается с предыдущим, "удаляем" который больше
            last = min(last, i[1])
            remove += 1

        return remove
