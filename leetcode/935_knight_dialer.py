class Solution:
    def knightDialer(self, n: int) -> int:
        m = 10 ** 9 + 7
        to = ((4, 6),  # moves from zero
              (8, 6),
              (7, 9),
              (4, 8),
              (3, 9, 0),
              (),
              (1, 7, 0),
              (2, 6),
              (1, 3),
              (2, 4),
              (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # moves from 10 - initial moves only
              )

        @cache
        def dive(pos, num):
            if pos == n:
                return 1
            res = 0
            for i in to[num]:
                res += dive(pos + 1, i)
            return res % (10**9 + 7)

        return dive(0, 10)
