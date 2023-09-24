from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # смотрим на два числа одинаковой длинны слева направо.
        # в том месте, где они начинают отличаться, там где меньшая цифра - то число раньше, оно меньше
        # как найти следующую перестановку?
        # берём убывающий (возрастающий справа) хвост, сортируем его (разворачиваем, он же убывает)
        # ищем в хвосте цифру, большую чем прехвост, и меняем её местами с прехвостом
        # те 1432 -> 1 432 -> 2 234 -> 2 1 34

        l = len(nums) - 1
        i = l
        while i >= 1:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        print(f'{i=}')
        pre = i - 1

        while i < l:
            print(f'{i=} {l=}')
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
            l -= 1

        if pre == -1:
            return

        for j in range(pre + 1, len(nums)):
            if nums[j] > nums[pre]:
                nums[pre], nums[j] = nums[j], nums[pre]
                return


print(Solution().nextPermutation([2, 3, 1]))
