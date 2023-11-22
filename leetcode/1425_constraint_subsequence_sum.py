from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        d = [0] * N
        max_q = deque()  # слева максимум, справа хвост

        for i in range(N):
            if i > k:
                if max_q[0] == d[i - k - 1]:  # сумма, которая была к элементов назад должна выпасть. если это наш максимум, то выпадает он
                    max_q.popleft()

            prev_max = max_q[0] if max_q else 0  # на первом шаге в деке ничего нет
            d[i] = max(prev_max, 0) + nums[i]  # предыдущюу сумму можно не брать

            while max_q and max_q[-1] < d[i]:  # из деки справа выкидываю всё, что меньше текущей суммы. оно точно не увеличит сумму на следующих шагах
                max_q.pop()
            max_q.append(d[i])

        return max(d)
