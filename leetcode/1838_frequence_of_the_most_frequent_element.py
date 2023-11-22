class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        accum = 0
        ans = 0

        for right, val in enumerate(nums):
            accum += val

            # пусть текущий элемент - будет самым частым. смотрим окошко до него.
            # текущий элемент умножить на длинну окошка должно быть меньше чем сумма в окошке + то, на сколько её можно увеличить
            # двигаем левую границу пока это не станет истинным
            while (right - left + 1) * val > accum + k:
                accum -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

