class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i, v in enumerate(nums):
            if (target - v) not in cache:
                cache[v] = i
            else:
                return [cache[target - v], i]
