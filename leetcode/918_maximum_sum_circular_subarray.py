from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def max_sub_array():
            current_sum = float('-inf')
            best_sum = float('-inf')

            for x in nums:
                current_sum = max(x, current_sum + x)
                best_sum = max(best_sum, current_sum)

            print(f'max best sum {best_sum}')

            return best_sum

        def min_sub_array():
            current_sum = float('inf')
            best_sum = float('inf')

            for x in nums:
                current_sum = min(x, current_sum + x)
                best_sum = min(best_sum, current_sum)

            print(f'min best sum {best_sum}')

            return best_sum

        best_circ = sum(nums) - min_sub_array()
        best_inner = max_sub_array()

        if best_circ == 0:
            return best_inner

        return max(best_inner, best_circ)

# как 53, только считаем не только сабэрэй с максимальной суммой, но ещё саэрей с минимальной суммой.
# если из всего эрея убрать сабэрей с минимальной суммой, то получится префикс и суфикс, те как раз циркулярный
