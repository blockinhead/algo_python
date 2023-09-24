from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast = 0
        slow = 0
        s = nums[slow]
        if s >= target:
            return 1

        res = float('inf')

        while slow < len(nums):

            if s < target:
                fast += 1
                if fast == len(nums):
                    break
                s += nums[fast]

            elif s >= target:
                res = min(res, fast - slow + 1)
                s -= nums[slow]
                slow += 1

        return res if isinstance(res, int) else 0


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
