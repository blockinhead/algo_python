class Solution:
    def minOperations(self, s: str) -> int:
        # 0101 first
        # 1010 second

        first = second = 0

        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '1':
                    first += 1
                else:
                    second += 1
            else:
                if c == '0':
                    first += 1
                else:
                    second += 1

        return min(first, second)
