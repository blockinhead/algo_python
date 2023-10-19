from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # табличка для дебага
        # dp = [[float('-inf')] * len(nums1) for _ in range(len(nums2))]

        @cache
        def max_dot_product(pos1, pos2):
            if pos1 < 0 or pos2 < 0:
                return float('-inf')

            # максимальный дотподукт = произведение текущих элементов + максимальный дотпродукт массивов покороче.
            # если дотпродукт коротких массивов отрицательный, то не будем его брать
            # в частности это сработает на границе
            res = nums1[pos1] * nums2[pos2] + max(0, max_dot_product(pos1 - 1, pos2 - 1))
            # но может быть получится число больше, если не возьмём текущие элементы, а возьмём массивы покороче
            # на границе это тоже будет работать хорошо
            res = max(res, max_dot_product(pos1 - 1, pos2))
            res = max(res, max_dot_product(pos1, pos2 - 1))

            # print(f'{pos1=} {pos2=} {res=}')
            # dp[pos2][pos1] = max(dp[pos2][pos1], res)

            return res

        r = max_dot_product(len(nums1) - 1, len(nums2) - 1)
        # for ro in dp:
        # print(ro)

        return r
