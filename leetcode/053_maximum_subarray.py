from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = float('-inf')

        for x in nums:
            current_sum = max(x, current_sum + x)  # если хвост уменьшает сумму, то отбросим его.
            # а текущему элементу уменьшеть сумму можно, ведь за ним может быть элемент, который увеличит сумму
            best_sum = max(best_sum, current_sum)

        return best_sum
