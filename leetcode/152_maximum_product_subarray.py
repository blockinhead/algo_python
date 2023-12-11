class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        accum = 1
        res = float('-inf')

        for v in nums:
            accum *= v
            res = max(res, accum)
            if v == 0:
                accum = 1

        accum = 1
        for v in nums[::-1]:
            accum *= v
            res = max(res, accum)
            if v == 0:
                accum = 1

        return res
