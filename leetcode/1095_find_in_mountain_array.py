# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        ar_len = mountain_arr.length()

        left = 0
        right = ar_len - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = mid + 1

        high = right
        print(f'{high=}')

        left = 0
        right = high
        while left <= right:
            mid = (left + right) // 2
            print(f'{left=} {right=} {mid=}')
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            if v < target:
                left = mid + 1
            else:
                right = mid - 1

        print('right')
        left = high + 1
        right = ar_len - 1
        while left <= right:
            mid = (left + right) // 2
            print(f'{left=} {right=} {mid=}')
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            if v > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

