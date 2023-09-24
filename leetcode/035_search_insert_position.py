from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low <= high:
            part = (high + low) // 2
            # print(f'{low=} {part=} {high=}')

            if part == len(nums):
                return part
            if nums[part] == target:
                return part
            if nums[part] < target:
                low = part + 1
            else:
                high = part - 1

        # print(f'{low=} {part=} {high=}')

        # после того как лоу и хай совпадут, парт будет такой же.
        # если таргет меньше этого числа, то лоу евеличиться на единицу, а это как раз то, что нужно.
        # а если таргет больше, то лоу останется как есть,
        # так что если число не найено, вставлять надо за лоу
        return low
