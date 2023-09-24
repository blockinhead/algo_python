from collections import deque


class Solution:
    def calculate(self, s: str, parenthesis=None) -> int:
        a = []
        for i in s:
            if i == ' ':
                continue
            if i in ('(', ')', '+', '-'):
                a.append(i)
                continue
            if i.isdigit():
                if a and a[-1].isdigit():
                    a[-1] += i
                else:
                    a.append(i)
        # print(a)

        acc = 0
        parenthesis_sign = 1
        prev_sign = 1
        sign_stack = deque()

        for e in a:
            if e == '(':
                sign_stack.append(prev_sign)
                if prev_sign < 0:
                    parenthesis_sign *= -1
                prev_sign = 1
            elif e == ')':
                if sign_stack.pop() < 0:
                    parenthesis_sign *= -1
            elif e == '+':
                prev_sign = 1
            elif e == '-':
                prev_sign = -1
            else:
                acc += int(e) * prev_sign * parenthesis_sign

        return acc




print(Solution().calculate(s=" 22-1 + 2 "))
print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)"))
