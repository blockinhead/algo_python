from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        le = len(nums)
        s = sorted(set(nums))

        res = le

        for left in range(len(s)):
            right = bisect_right(s, s[left] + le - 1)
            window = right - left

            res = min(res, le - window)

        return res

# чтобы массив был непрерывный, нужно чтобы цифр в нём были все цифры от н до н + длинна массива - 1
# пробуем искать окошко, в котором содержится непрерываня последовательность, то есть искать надо в отсортированном сете
# берём левый край, тогда правый край должен быть равен левый + длинна. раздвигаем окно в этих пределах
# длинна массива - длинна окна = количество изменений, которые нужно внести
