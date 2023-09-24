from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [1] * len(nums)

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    d[i] = max(d[i], d[j] + 1)

        return max(d)
