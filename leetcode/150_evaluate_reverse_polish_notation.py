from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = deque()

        ops = {'+': lambda a, b: a + b,
               '-': lambda a, b: b - a,
               '*': lambda a, b: a * b,
               '/': lambda a, b: int(b / a)}

        for v in tokens:
            if v not in ops:
                d.append(int(v))
                continue

            # arg1 = d.pop()
            # arg2 = d.pop()
            # res = ops[v](arg1, arg2)
            # d.append(res)
            d.append(ops[v](d.pop(), d.pop()))

        return d[0]


# print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
