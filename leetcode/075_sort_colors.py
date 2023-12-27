class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twoes = 0

        for v in nums:
            if v == 0:
                zeroes += 1
                continue
            if v == 1:
                ones += 1
                continue
            twoes += 1

        i = 0
        for _ in range(zeroes):
            nums[i] = 0
            i += 1

        for _ in range(ones):
            nums[i] = 1
            i += 1

        for _ in range(twoes):
            nums[i] = 2
            i += 1
