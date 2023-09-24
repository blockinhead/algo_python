import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        dt = collections.Counter(t)
        if (sr := s[right]) in dt:
            dt[sr] -= 1

        res = ' ' * (len(s) + 1)

        while left < len(s):
            if self.empty(dt):
                if len(res) > right - left:
                    res = s[left: right + 1]

                if (sl := s[left]) in dt:
                    dt[sl] += 1
                left += 1

                continue

            else:
                if right == len(s) - 1 and not self.empty(dt):
                    break

                right += 1
                if (sr := s[right]) in dt:
                    dt[sr] -= 1

        if res[0] == ' ':
            return ''

        return res

    def empty(self, d):
        for k, v in d.items():
            if v > 0:
                return False

        return True


print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
