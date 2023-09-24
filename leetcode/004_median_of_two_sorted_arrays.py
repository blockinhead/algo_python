from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        # интервал бинарного поиска
        start = 0
        end = x

        while True:
            px = (end + start) // 2  # бинарный поиск в первом массиве
            # разбиение второго массива считаем так,
            # чтобы суммарно слева и справа было поровну
            # (или слева было на одно число больше, если всего чисел нечётно)
            py = (x + y + 1) // 2 - px

            # если двигать некуда, то можно сравнить с бескончностями, там неравенства всегда будут выполнятся нормально
            nums1_left_part_max = nums1[px - 1] if px > 0 else float('-inf')
            nums1_right_part_min = nums1[px] if px < x else float('inf')
            nums2_left_part_max = nums2[py - 1] if py > 0 else float('-inf')
            nums2_right_part_min = nums2[py] if py < y else float('inf')


            if nums1_right_part_min >= nums2_left_part_max and nums2_right_part_min >= nums1_left_part_max:
                # равновесие найдено
                if (x + y) % 2:
                    # когда всего чисел нечётно, мелиана лежит в левой части
                    return max(nums1_left_part_max, nums2_left_part_max)
                else:
                    return (max(nums1_left_part_max, nums2_left_part_max) + min(nums1_right_part_min, nums2_right_part_min)) / 2

            if nums1_left_part_max > nums2_right_part_min:
                end = px - 1
            else:
                start = px + 1  # равновесие надо искать правее в первом массиве


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

'''
from  typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1  # make nums2 shorter

    lo = 0
    hi = len(nums2) * 2

    while lo <= hi:
        mid2 = (lo + hi) // 2
        mid1 = len(nums1) + len(nums2) - mid2

        l1 = float('-inf') if mid1 == 0 else nums1[(mid1 - 1) // 2]
        l2 = float('-inf') if mid2 == 0 else nums2[(mid2 - 1) // 2]
        r1 = float('inf') if mid1 == len(nums1) * 2 else nums1[mid1 // 2]
        r2 = float('inf') if mid2 == len(nums1) * 2 else nums2[mid2 // 2]

        if l1 > r2:
            lo = mid2 + 1
        elif l2 > r1:
            hi = mid2 - 1
        else:
            return (max(l1, l2) + min(r1, r2)) / 2

    return -1





print(findMedianSortedArrays(None, [1, 3], [2]) == 2)
print(findMedianSortedArrays(None, [1, 2], [3, 4]) == 2.5)
'''
