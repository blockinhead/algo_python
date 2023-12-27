class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        def dive(i, j):
            if i >= n and j >= m:
                return True

            if i >= n and p[j:].lstrip('*') == '':
                return True

            if i < n and j >= m:
                return False

            if i >= n and j < m:
                return False

            if s[i] == p[j] or p[j] == '?':
                return dive(i + 1, j + 1)

            if p[j] == '*':
                return dive(i + 1, j) or dive(i, j + 1) or dive(i + 1, j + 1)

            return False

        return dive(0, 0)


# print(Solution().isMatch('aa', 'a'))
# print(Solution().isMatch('aa', '*'))
# print(Solution().isMatch('cb', '?a'))
print(Solution().isMatch('', '**'))
