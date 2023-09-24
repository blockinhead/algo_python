class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        k = 0
        while True:
            # print(f'{left:b} {right:b}')
            if left != right:
                left = left >> 1
                right = right >> 1
                k += 1
            else:
                break

        # print(f'{k=}, {left:b} {(left >> k):b}')

        return left << k

# выпишем бинарное представление всех чисел диапозона в столбик
# левая часть столбика будет меняться. правая - нет.
# там де есть изменения в результате будет 0, тк достаточно одного нуля чтобы занулить весь столбик
# ищем правую часть сдвигом. потом дивгаем её обратно
