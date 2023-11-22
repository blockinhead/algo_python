from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        d = deque()
        d.append('')
        mults = deque()
        num = 0

        for c in s:
            # коплю число, увеличиваю разряд
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            # началось слово. сбрасываю число в стек чисел, создаю место под слово
            if c == '[':
                mults.append(num)
                num = 0
                d.append('')
                continue

            # слово закончилось. накопленное слово домножаю на число, дописываю его к внешнему (на верхнем уровне пустому) слову
            if c == ']':
                w = d.pop() * mults.pop()
                d[-1] += w
                num = 0
                continue

            # это буква. дописываю её к текущему слову
            d[-1] += c

        return ''.join(d)


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))

# красивый вариант - копить всё до закрывающей квадратной скобки.
# когда нашёл скобку - разматываю обратно накопленное слово до открывающей скобки,
# домножаю на цифру перед открывающей скобкой
# закидываю то, что получилось в стек, ищю следующую закрывающую скобку в исходном слове...
