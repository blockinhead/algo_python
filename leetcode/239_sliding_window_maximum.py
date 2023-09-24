from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()  # в деку быстро добавлять и удалять слева и справа

        # сначала набиваем окошко. если текущее число больше, чем те, которые уже есть в деке справа,
        # то выкидываем их оттуда
        # новое число кладём в деку в любом случае, ведь предыдущее число, даже если оно было больше, уйдёт,
        # когда окошко сдвинется
        # но если потом придёт число меньше левого, но больше предыдущего, то мы выкинем его
        for i in range(k):
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)

        # индекс самого большого числа будет слева, ведь все числа меньше этого мы викидывали при добавлении
        res.append(nums[d[0]])

        for i in range(k, len(nums)):
            # окошко сдвинулось, максимум выпал.
            # максимумом текущего окошка будет либо следующ и элемент из деки,
            # или текущий элемент, если текущий элемент больше всего, что лежит в деке
            if d[0] == i - k:
                d.popleft()

            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)

            res.append(nums[d[0]])

        return res


print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 4))

'''
в деке всегда максимум будет слева, а текущий элемент справа
# nums = [1,3,-1,-3,5,3,6,7], k = 4
первый цикл. 
1. дека пустая. добавляем индекс 1
2. выкидываем индекс 1, потому что 3 больше, 3 новый максимум окна, 1 точно не понадобится
3. добавялем индекс -1. ничего не выкидываем, потому что -1 меньше 3. но она может быть максимумом, когда 3 выпадет из окна
4. добавляем индекс -3. соображения такие же, как на третем шагу
доавляем в результат то, индекс чего слева, те 3
следующий цикл. окно поползло вперёд.
i = 4:
из окна ничего не выпадает. единицу мы удалили на втором шаге предыдущего цикла.
но текущий элемент - 5, которая больше, чем всё, что лежит в деке. 
то есть 5 - это новый максимум текущего окна. ни 3, которая выпала бы на следующем шаге, ни -1 которая могла бы быть максимумом после выпадения тройки, ни -3, все они уже точно не пригодятся
5 будет максимумом окошек, которые начинаются и с 3, и с -1 и с -3
i = 5
из окна ничего не выпадает.
текущий элемент - 3. она меньше, чем 5, так что мы ничего не удаляем и мы кладём его в деку. 3 может быть максимумом, когда 5 выпадет
а максимум текущего окошка - 5, его индекс слева
i = 6
из окна ничего не выпадает.
текущий элемент - 6. новый максимум. выкидываем индексы 3 и 5
...
'''