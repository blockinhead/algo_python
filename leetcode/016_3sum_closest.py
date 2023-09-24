from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        c = float('inf')
        res = 0

        for i in range(len(nums) - 2):

            low = i + 1
            high = len(nums) - 1

            while low < high:
                s = nums[i] + nums[low] + nums[high]
                # print(f'{nums[i]=} {nums[low]=} {nums[high]=}')
                if c > (c_ := abs(target - s)):
                    print(f'{s=}')
                    c = c_
                    res = s
                if s < target:  # недолёт. нужно увеличить сумму. то есть подвинуть левый указатель в сторону числе побольше
                    low += 1
                else:  # перелёт. попробуем взять третим компонентом число поменьше
                    high -= 1

        return res
