class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        vals_count = [0] * (5 * 10 ** 4 + 1)

        nums_max = 0
        nums_min = 5 * 10 ** 4 + 1
        for v in nums:
            vals_count[v] += 1
            nums_min = min(nums_min, v)
            nums_max = max(nums_max, v)

        res = 0
        acc = 0
        for i in range(nums_max, nums_min, -1):
            v = vals_count[i]
            if v == 0:
                continue
            acc += v
            res += acc

        return res

# опустим все максимальные числа на одну ступеньку до предыдущего значения.
# сколько таких числе запишем в акк
# числа чуть меньше тоже опустим  на ступеньку вниз. большие числа тоже. сколько всего мы их опускаем - написано в акк
# и так до минимального числа не включительно
