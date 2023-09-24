from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # половина любого интервала точно отсортирована по возрастанию
            # в отсортированной опловине мы можем поискать наш таргет. если он там, то бинарный поиск туда.
            # если нет, то бинарный поиск в другую половину
            if nums[low] <= nums[mid]:
                # если отсортирована нижняя половина, ищем таргет в ней
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # иначе отсортирована верхняя половина, ищем там
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
