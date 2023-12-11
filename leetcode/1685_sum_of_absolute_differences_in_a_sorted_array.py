class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # x = nums[i]
        # (x - a) + (x - b) + (x - c) + (x - x) + (d - x) + (e - x) + (f - x)
        # x * n - prev_sum + post_sum - x * m

        n = 0
        prev = 0
        m = len(nums)
        post = sum(nums)
        res = []

        for x in nums:
            prev += x
            n += 1
            res.append(x * n - prev + post - x * m)
            post -= x
            m -= 1

        return res
