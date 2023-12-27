class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m = pm = 101

        for p in prices:
            if p < m:
                pm = m
                m = p
            elif p < pm:
                pm = p

        res = money - m - pm

        if res >= 0:
            return res
        return money
