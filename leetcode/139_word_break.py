from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        d = [False] * (len(s) + 1)
        d[0] = True

        for i in range(1, len(s) + 1):
            wo = s[:i]
            for w in wordDict:
                ws = w
                if i < len(w):
                    continue
                tt = i - len(w)
                bb = d[i - len(w)]
                if not d[i - len(w)]:
                    continue

                sss = s[i - len(w): i]
                if s[i - len(w): i] == w:
                    d[i] = True
                    break

        print(d)

        return d[-1]


print(Solution().wordBreak('leecod', ['lee', 'cod']))
print(Solution().wordBreak('a', ['b']))
