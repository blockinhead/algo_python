class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half, rem = divmod(sum(nums), 2)
        if rem != 0:
            return False

        nums.sort()

        @cache
        def dive(i, cur_sum):
            if cur_sum == half:
                return True
            if cur_sum > half:
                return False
            if i >= len(nums):
                return cur_sum == half

            return dive(i + 1, cur_sum + nums[i]) or dive(i + 1, cur_sum)

        return dive(0, 0)
