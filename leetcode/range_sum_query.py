# encoding: utf8
# класс, который позволяет искать частичную сумму массива
# для этого создаём словарь с полной суммой до данного индекса

class NumArray:

    def __init__(self, nums: list[int]):
        self._sum_parts = {}
        s = 0
        for i, v in enumerate(nums):
            s += v
            self._sum_parts[i] = s
        print(self._sum_parts)

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self._sum_parts[right]

        return self._sum_parts[right] - self._sum_parts[left-1]


na = NumArray([-2,0,3,-5,2,-1])
print(na.sumRange(0, 2))
print(na.sumRange(2, 5))
print(na.sumRange(0, 5))
