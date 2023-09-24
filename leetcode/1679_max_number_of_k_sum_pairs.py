# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations_(self, nums: List[int], k: int) -> int:
        counter = 0
        d = defaultdict(int)
        for n in nums:
            if d[-n]:
                counter += 1
                d[-n] -= 1
            else:
                d[n - k] += 1

        return counter

    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        d = {}
        for n in nums:
            if d.get(-n):
                counter += 1
                d[-n] -= 1
            else:
                d[n - k] = d.get(n - k, 0) + 1

        return counter


if __name__ == '__main__':
    sol = Solution()
    print(2, sol.maxOperations([1, 2, 3, 4], 5))
    print(1, sol.maxOperations([3, 1, 3, 4, 3], 6))


