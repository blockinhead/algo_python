class Solution:
    def numberOfMatches(self, n: int) -> int:
        r = 0
        while n > 1:
            if n % 2:
                n = (n - 1) // 2
                r += n
                n += 1
            else:
                n = n // 2
                r += n

        return r
