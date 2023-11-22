from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        i = j = k
        res = nums[k]
        current_min = nums[k]

        while i != 0 or j != N - 1:
            # смотрю, какое число можно доавить к окну так, чтобы не сильно ухудшать результат
            # хочу добавлять то число, которое больше. оно точно увеличит ширину окна, что максимизирует произведение, и может при этом не минимизирует текущее минимальное значение в окне
            to_right = nums[
                j + 1] if j + 1 < N else 0  # если уже граница, то противоположную часть окна можно смело сравнивать с нулём, все числа в массиве положительные
            to_left = nums[i - 1] if i - 1 >= 0 else 0
            if to_right > to_left:
                j += 1
                current_min = min(current_min, to_right)
            else:
                i -= 1
                current_min = min(current_min, to_left)

            # print(f'{i=} {j=} {current_min=}')

            res = max(res, current_min * (j - i + 1))

        return res
