from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = deque()
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            print(f'{i=} {v=} {d=}')
            while d and d[-1][0] < v:
                _, prev_i = d.pop()
                res[prev_i] = i - prev_i

            d.append((v, i))

        return res


# как только я нашёл температуру больше, чем в конце деки, я могу сказать,
# сколько дню в конце деки ждать следующего более тёплого дня
# так уберу из деки все более холодные дни, чем текущий
# добавлю текущий день
# так получится возрастающая очередь
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
