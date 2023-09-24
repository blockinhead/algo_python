from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(len(nums) - k + 1):
            res = heappop(nums)

        return res
