class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = 10 ** 9 + 7

        @cache
        def dive(cube_n, prev_sum):
            if cube_n == n:
                if prev_sum == target:
                    return 1
                return 0

            res = 0
            for i in range(1, k + 1):
                res += dive(cube_n + 1, prev_sum + i)

            return res % m

        return dive(0, 0)
