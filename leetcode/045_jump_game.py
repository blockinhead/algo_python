from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        num_jumps_to = [float('inf')] * len(nums)
        num_jumps_to[0] = 0
        # num_jumps_to[1] = 1

        for i in range(len(nums)):
            next_jumps = range(i + 1, min(i + nums[i] + 1, len(nums)))
            next_jumps = list(next_jumps)
            for j in next_jumps:
                num_jumps_to[j] = min(num_jumps_to[j], num_jumps_to[i] + 1)

        return num_jumps_to[-1]


print(Solution().jump([1, 1, 1, 1, 1, 1]))

