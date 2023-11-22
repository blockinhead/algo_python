class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        '''
        # тут не хватает памяти для очень длинных строк
        @cache
        def lcs(a, b):
            if not a or not b:
                return 0

            if a[0] == b[0]:
                return 1 + lcs(a[1:], b[1:])
            return max(lcs(a, b[1:]), lcs(a[1:], b))

        return lcs(text1, text2)
        '''

        r1 = len(text1)
        r2 = len(text2)

        d = [[0] * (r1 + 1) for _ in range(r2 + 1)]

        '''
        в д кладу максимальную длинну пересечения подстрок, которые заканчиваются на буквы л1 и л2
        если буквы под индексами л1 и л2 равны, то эта длинна равна максимальной длинне пересечения без этих букв + 1
        если не равны, то смотрим на подстроки без одной из этих букв или без обеих
        если мы смотрим первую букву слова, то слово без этой буквы - пустое слово. длинна пересечения с ним ноль. по идее первая строка и левый столбец должны состоять из нулей
        но питон позволяет смотреть по отрицательным индексам, так что эти нули я положил в последнюю строку и правый столбец, увеличив таблицу на одну строку и один столбец не сверху и слева, а снизу и справа
        '''

        for l2 in range(r2):
            for l1 in range(r1):
                s = 1 if text1[l1] == text2[l2] else 0
                d[l2][l1] = max(s + d[l2 - 1][l1 - 1], d[l2 - 1][l1], d[l2][l1 - 1])

        return d[-2][-2]
