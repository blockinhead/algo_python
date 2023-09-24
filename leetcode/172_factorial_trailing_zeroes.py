class Solution:
    def trailingZeroes(self, n: int) -> int:
        # ноль даёт умножение на десять. десять - это 2х5 двоек в составляющих факториала явно больше чем пятёрок, так что надо просто посчитать сколько там пятёрок

        if n < 5:
            return 0

        res = 0

        while n != 0:
            t = n // 5
            res += t
            n = t

        return res

    