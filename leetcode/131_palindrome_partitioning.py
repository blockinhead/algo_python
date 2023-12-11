class Solution:

    def partition(self, s: str) -> List[List[str]]:
        parts = []
        res = []

        def dive(i):
            if i >= len(s):
                print(f'{parts=}')
                res.append(parts[:])
                return

            for j in range(i, len(s)):
                if s[i: j + 1] == s[i: j + 1][::-1]:
                    parts.append(s[i: j + 1])
                    dive(j + 1)
                    parts.pop()

        dive(0)
        return res


