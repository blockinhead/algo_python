from functools import cache
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @cache
        def get_cost(wall, num_unpainted):
            if num_unpainted <= 0:  # всё покрасили
                return 0
            if wall == len(cost):  # дошли до последней стены, но покрашено не всё - плохой вариант
                return float('inf')

            # можно покрасить это стену за cost[wall], тогда останется покрасить remainig - 1 (та стена, которую красим) - time[wall] (столько стен покрасит второй художник бесплатно)
            paint = cost[wall] + get_cost(wall + 1, num_unpainted - 1 - time[wall])
            # можно не красить эту стену, перейти к следующей, тогда количество непокрашеных стен не изменится
            not_paint = get_cost(wall + 1, num_unpainted)

            return min(paint, not_paint)

        return get_cost(0, len(cost))
