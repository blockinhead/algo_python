from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        q = deque()

        for b in s:
            if b in d:
                q.append(d[b])
            else:
                if not q:
                    return False
                if b != q.pop():
                    return False

        if len(q):
            return False

        return True


print(Solution().isValid(s="()[]{}"))
