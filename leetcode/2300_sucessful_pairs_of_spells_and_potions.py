class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = [0] * len(spells)
        p = len(potions)

        for i, v in enumerate(spells):
            left = bisect_left(potions, success / v)
            res[i] = p - left

        return res
