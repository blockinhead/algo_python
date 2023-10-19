from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def step(i):
            # чтобы попасть на первые две ступеньки ничего платить не надо
            if i < 2:
                return 0

            # чтобы попасть на и-ую ступеньку надо либо попасть на предыдущую и заплатить,
            # либо на предпредыдущую и заплатить
            v1 = step(i - 1) + cost[i-1]
            v2 = step(i - 2) + cost[i-2]
            return min(v1, v2)

        return step(len(cost))


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
