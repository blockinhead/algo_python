class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = float('-inf')

        for v in nums:
            if v > m1:
                m2 = m1
                m1 = v
            elif m2 < v <= m1:
                m2 = v
            # print(f'{v} {m1=} {m2=}')

        return (m1 - 1) * (m2 - 1)
