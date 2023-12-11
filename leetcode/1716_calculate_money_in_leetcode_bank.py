class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        res = 0

        # 1+2+3+4+5+6+7 = 28
        for i in range(weeks):
            res += 28 + (i * 7)

        for i in range(days):
            res += (i + 1) + weeks

        return res
