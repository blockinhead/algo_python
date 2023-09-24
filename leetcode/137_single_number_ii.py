class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 1
        res = 0

        neg = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                neg += 1
            nums[i] = abs(nums[i])
        # так как я не справился с отрицательными числами на уровне битов, работать считать положительные

        for _ in range(32):
            ones = 0

            for i in range(len(nums)):
                print(f'{nums[i]:b} {nums[i] & mask:b}')
                if mask & nums[i] == 1:
                    ones += 1

                nums[i] = nums[i] >> 1

            print(f'{ones=} {ones % 3 =}')
            if ones % 3:
                # print('adding one and moving')
                res = res | (1 << 32)
            res = res >> 1
            print(f'{res:b}')

        return -res if neg % 3 else res

# смотрим количество единичек в первом разряде. если оно не кратно трём, то у лишнего числа в этом разряде единичка
# двигаем числа влево
# у результата самый левый разряд выставляем в соответствии с подчитанным количеством единиц. за 32 итерации первый разряд как раз встанет на место
