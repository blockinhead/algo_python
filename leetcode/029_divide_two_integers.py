class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = False
        if dividend < 0 and divisor > 0:
            sign = True
            dividend = -dividend

        elif dividend >= 0 and divisor < 0:
            sign = True
            divisor = -divisor

        elif dividend <= 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend

        # print(f'{dividend=} {divisor=}')

        if divisor == 1:
            r = dividend if not sign else -dividend
            return max(min(r, (2 ** 31 - 1)), -2 ** 31)

        a = dividend
        b = divisor
        # нужно посчитать сколько раз a умещается в b
        res = 0

        while a >= b:
            tmp_b = b
            c = 1

            while a >= tmp_b:
                a -= tmp_b
                res += c
                c += c
                tmp_b += tmp_b
                # будем пробовать увеличивать знаменатель в два раза.
                # когда он перестанет умещаться в числителе, вернёмся к начальному знаменателю. так получится логарифмическая скорость

        if sign:
            res = -res

        return max(min(res, (2 ** 31 - 1)), -2 ** 31)


print(Solution().divide(10, 3))
