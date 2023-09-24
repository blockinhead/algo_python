# encoding: utf8
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class SolutionMy:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numt = sorted(nums)
        i = 0
        while nums[i] == numt[i]:
            i += 1
            if i == len(nums):
                return 0

        j = len(nums) - 1
        while nums[j] == numt[j]:
            j -= 1
            if j == -1:
                return len(nums)

        res = (j + 1) - i
        return res

# ищем минимальную неупорядоченную подпоследовательность в упорядоченном по возрастанию списке
# как найти конец?

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        end = -1
        max_val_from_beginning = nums[0]
        start = 0
        min_val_from_end = nums[-1]

        for i in range(len(nums)):
            if max_val_from_beginning <= nums[i]:  # двигаемся вперёд, забираемся на холмик вверх
                max_val_from_beginning = nums[i]   # пока новый шаг выше чем предыдущий, всё ок, список отсортирован
            else:                                  # но если вдруг мы ниже достигнутой вершины, то упорядоченость в этом месте нарушена
                end = i                            # будем двигать конец неупорядоченого подмассива

            if min_val_from_end >= nums[~i]:  # двигаемся назад, спускаемся вниз
                min_val_from_end = nums[~i]   # пока новый шаг ниже чем предыдущий, список отсортирован
            else:                             # но если вдруг встретилось что-то большее, чем минимум по предыдущим шагам, то тут уже неотсортировано
                start = ~i

        start = len(nums) + start
        res = end - start + 1
        return max(0, res)


if __name__ == '__main__':
    sol = Solution()
    assert sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert sol.findUnsortedSubarray([1, 2, 3, 4]) == 0
    assert sol.findUnsortedSubarray([1]) == 0
    assert sol.findUnsortedSubarray([2, 1]) == 2
