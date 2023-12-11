class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = ''
        for a, b, c in zip(num, num[1:], num[2:]):
            if a == b == c and a > prev:
                prev = a

        return prev * 3
