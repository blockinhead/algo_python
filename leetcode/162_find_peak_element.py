from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1

        if len(nums) <= 2:
            return nums.index(max(nums))

        while first < last:
            mid = (first + last) // 2
            # if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                # return mid

            if nums[mid] > nums[mid + 1]:
                last = mid
            else:
                first = mid + 1

        return first
