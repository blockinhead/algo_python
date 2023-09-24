from collections import defaultdict
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        pairs = defaultdict(set)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                pairs[nums[i] + nums[j]].add((i, j))

        res = set()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                if (v := target - (nums[i] + nums[j])) not in pairs:
                    continue

                for k, l in pairs[v]:
                    if not (i < j < k < l):
                        continue

                    res.add((nums[i], nums[j], nums[k], nums[l]))

        return res
