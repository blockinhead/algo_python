from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def count_ways(current_index, steps_left):
            if steps_left == 0:
                if current_index == 0:
                    return 1
                return 0

            res = 0
            if current_index >= 0:
                res += count_ways(current_index + 1, steps_left - 1)
            if current_index < arrLen:
                res += count_ways(current_index - 1, steps_left - 1)
            res += count_ways(current_index, steps_left - 1)

            return res % mod

        return count_ways(0, steps)

