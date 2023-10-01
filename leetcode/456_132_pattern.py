from collections import deque, namedtuple
from typing import List


Window = namedtuple('Window', ['low', 'high'])


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cur_mi = nums[0]
        windows = deque()
        # если смотреть на окошко, текущий элемент может быть
        # либо ниже окошка, тогда он может стать нижней границей нового окошка,
        # либо попадать в окошко, тогда мы нашли ответ,
        # либо выше окошка, тогда у нас будет новое более широкое окошко

        # это не окошко, но оно быстро выкенется, или уйдёт вниз стека
        windows.append(Window(nums[0], nums[0]))

        for i in range(1, len(nums)):
            new_v = nums[i]

            # новое окошко строим от текущего минимума. если новый элемент ниже,
            # то это будет новый текущий минимум
            if new_v <= cur_mi:
                cur_mi = new_v
                continue

            # новый элемент выше текущего минимума, но ниже предыдущего окна - будет новое окно
            if new_v < windows[-1].low:
                windows.append(Window(cur_mi, new_v))
                continue


            # новый элемент выше текущего минимума
            while windows:
                # если последнее окно уже чем новое - просто выкинем его
                if windows[-1].low >= cur_mi and windows[-1].high <= new_v:
                    windows.pop()
                    continue
                # если новый элемент попадает в окно, то мы нашли ответ
                if windows[-1].low < new_v < windows[-1].high:
                    return True

                # если я дошёл сюда, то все окошки, уже чем новое, мы выкинули,
                # но патерна 132 при этом не нашли
                break

            # добавим новое окошко
            windows.append(Window(cur_mi, new_v))

        return False


print(Solution().find132pattern([3, 5, 0, 3, 4]))
print(Solution().find132pattern([3, 5, 0, 1, 2, 4]))
print(Solution().find132pattern([-2, 1, -2]))
