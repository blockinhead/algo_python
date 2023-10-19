from functools import cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # максимум должен обновляться ровно к разю те перед m должно быть к чисел любых дрругих чисел (м - это максимум)

        # низходящее динамическое программирование
        @cache
        def num_arrays(current_pos, current_max, current_k):

            # если мы дошли до массива длинны 0, то есть весь массив был построен,
            # при этом количество обновлений максимума 0, то есть все обновления тоже были совершены,
            # то мы построили хороший массив, посчитаем его
            if current_pos == 0:
                if current_k == 0:
                    return 1
                return 0

            num_good_arrays = 0
            for i in range(1, m + 1):
                # попробуем на предыдущее место поставить число от 1 до м
                # если это число меньше текущего максимума, то обновления максимума не будет
                if i <= current_max:
                    num_good_arrays += num_arrays(current_pos - 1, current_max, current_k)
                else:  # i > current_max
                    # обновили максимум, использовали одно обновление
                    num_good_arrays += num_arrays(current_pos - 1, i, current_k - 1)
            return num_good_arrays

        return num_arrays(n, 0, k) % (10 ** 9 + 7)
