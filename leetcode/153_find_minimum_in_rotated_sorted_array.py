from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return min(nums)


        low = 0
        high = len(nums) - 1

        while low < high:
            # массив был отсортирован и повёрнут. то есть в его хвосте числа меньше чем в начале
            # если мы нашли кусок, где это не так, то минимум слева
            if nums[low] < nums[high]:
                return nums[low]

            mid = (low + high) // 2
            # mid = int(low + (high - low) / 2)
            print(f'{mid=} {low=} {high=}')

            if nums[low] <= nums[mid]:  # это отсортированный кусок, минимум не в нём, он правее
                low = mid + 1
            else:
                high = mid

            print(f'{mid=} {low=} {high=}')

        return nums[low]
