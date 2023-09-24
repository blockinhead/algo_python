class Solution:
    def myAtoi(self, s: str) -> int:
        LOW = 2 ** 31
        HIGH = LOW - 1

        s = s.split()
        if not s:
            return 0

        s = s[0]

        positive = True
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            positive = False
            s = s[1:]

        if s and not s[0].isdigit():
            return 0

        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break

        res = 0
        for i in range(len(s)):
            res += int(s[-i - 1]) * (10 ** i)
            if not positive and res >= LOW:
                return -LOW
            if positive and res >= HIGH:
                return HIGH

        return res if positive else -res
