class Solution:
    def numDecodings(self, s: str) -> int:
        # nums = {str(i) for i in range(1, 27)}
        first = '123456789'
        # second_one = '1'
        # second_two = '0123456'

        @cache
        def dive(pos):
            if pos == len(s):
                return 1

            if pos > len(s) or s[pos] == '0':
                return 0

            res = 0
            if s[pos] in first:
                 res += dive(pos + 1)

            if pos + 2 <= len(s) and 1 <= int(s[pos:pos+2]) <= 26:
                res += dive(pos + 2)

            return res

        return dive(0)
