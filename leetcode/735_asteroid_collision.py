from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        d = deque()
        i = 0

        while i < len(asteroids):

            a = asteroids[i]
            prev = d[-1]

            # если астераиду не столкнётся с предыдщим
            # стек пустой, или астероиды двигаются в одну сторону, или предыдущий налево и текущий направо
            if not d or (prev * a > 0) or (prev < 0 and a > 0):
                d.append(a)
                i += 1
                continue

            # else d[-1] > 0 and a < 0:
            if prev == -a:
                d.pop()
                i += 1
                continue

            if prev > -a:
                i += 1
                continue

            # if  d[-1] < a:
            d.pop()

        return d


# print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
