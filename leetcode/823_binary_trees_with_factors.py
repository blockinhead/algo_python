from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mo = 10 ** 9 + 7

        arr.sort()

        nums = set(arr)

        d = {x: 1 for x in nums}  # сколько есть способов построить дерево для числа х

        for i in arr:
            for j in arr:
                if i % j == 0 and (v := i // j) in nums:
                    # если число i можно преставить как произведение чисел, которые тоже есть в массиве
                    # то для него можно построить деревья
                    d[i] += d[j] * d[v]
                    d[i] %= mo

        return sum(d.values()) % mo
