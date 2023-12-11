from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        # @cache
        def dive(i, j):
            if i >= n and j >= m:
                return True

            if i < n and j >= m:
                return False

            chars_match = i < n and (s[i] == p[j] or p[j] == '.')

            if j < m - 1 and p[j + 1] == '*':
                # если следующий символ регулярки - звёздочка
                # то надо посмотреть два варианта -
                # 1. если текущий символ сматчился, то перейти к следующему символу строки
                # 2. вне зависимости от того, сматчился ли текущий симво, попробовать перестпуть в регулярке за звёздочку,
                # ведь звёздочка означает _ноль_ или более текущих символов
                return (chars_match and dive(i + 1, j)) or (dive(i, j + 2))

            if chars_match:
                return dive(i + 1, j + 1)

            return False  # сюда мы попадём, если строка кончилась, регулярка ещё нет и её текущий символ - не звёздочка

        return dive(0, 0)


# print(Solution().isMatch('aa', 'a*'))
# print(Solution().isMatch('abb', 'a.*'))
print(Solution().isMatch('ab', '.*c'))
print(Solution().isMatch('aaa', 'a*a'))
