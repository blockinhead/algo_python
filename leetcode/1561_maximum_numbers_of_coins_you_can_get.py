class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        res = 0

        left = 1
        right = len(piles) - 1

        while left < right:
            res += piles[left]
            left += 2
            right -= 1

        return res


# 8 7 4 2 2 1