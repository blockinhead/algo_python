class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        res = []

        for left, right in zip(l, r):
            buf = nums[left: right + 1]
            buf.sort()
            res.append(True)
            step = buf[1] - buf[0]
            for i in range(1, len(buf)):
                if buf[i] - buf[i - 1] != step:
                    res[-1] = False
                    break

        return res
