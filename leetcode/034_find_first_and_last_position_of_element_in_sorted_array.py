from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        else:
            return [-1, -1]

        found = mid

        low = 0
        high = found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                break

            if nums[mid] == target:
                high = mid - 1
            else:
                low = mid + 1

        res_l = mid

        low = found
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                break

            if nums[mid] == target:
                low = mid + 1
            else:
                high = mid - 1

        res_h = mid

        return [res_l, res_h]

