from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        d = deque()
        for c in s:
            if c == '*':
                d.pop()
                continue

            d.append(c)

        return ''.join(d)
