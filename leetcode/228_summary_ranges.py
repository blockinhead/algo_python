from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        left = 0
        right = 0
        counter = 0
        res = []

        while right < len(nums):
            right += 1
            counter += 1
            if right < len(nums) and nums[right] == nums[left] + counter:
                continue

            if left == right - 1:
                res.append("%d" % nums[left])
            else:
                res.append("%d->%d" % (nums[left], nums[min(right - 1, len(nums) - 1)]))
            left = right
            counter = 0

        return res

print(Solution().summaryRanges(nums = [0,1,2,4,5,7]))
