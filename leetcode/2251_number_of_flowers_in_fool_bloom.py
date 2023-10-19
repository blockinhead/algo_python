from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def _fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(x for x, _ in flowers)
        finishes = sorted(y for _, y in flowers)
        print(f'{starts=}')
        print(f'{finishes=}')

        counter = 0
        res = [0] * len(people)
        # print(f'{res=}')
        day = 0
        s = 0
        f = 0
        for i, visitor in sorted(enumerate(people), key=lambda x: x[1]):
            print(f'{visitor=} {i=}')
            while day <= visitor:
                while s < len(starts) and starts[s] == day:  # цветы, которые зацвели сегодня
                    counter += 1
                    s += 1

                while f < len(finishes) and finishes[f] < day:
                    # цветы, котоорые отцвели вчера. на самом деле можно не < , а == day - 1
                    counter -= 1
                    f += 1

                day += 1

            res[i] = counter

        return res

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(x for x, _ in flowers)
        finishes = sorted(y for _, y in flowers)
        print(f'{starts=}')
        print(f'{finishes=}')

        res = [0] * len(people)

        for i, visitor in enumerate(people):
            # бинарный поиск в цикле оказывается быстрее, чем один раз перебрать весь массив
            # бисект-райт - сколько цветов зацветало включая текущий день
            # бисект-лефт - сколько цветов отцвело не включая текущий день
            f = bisect_right(starts, visitor) - bisect_left(finishes, visitor)
            res[i] = f

        return res


# print(Solution().fullBloomFlowers(flowers=[[1,6],[3,7],[9,12],[4,13]], people=[2,3,7,11]))
print(Solution().fullBloomFlowers(flowers=[[1,10],[3,3]], people=[3,3,2]))

