class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        for w in path.split('/'):
            if not w:
                continue
            if w == '.':
                continue
            if w == '..':
                if res:
                    res.pop()
                continue

            res.append(w)

        return '/' + '/'.join(res)


print(Solution().simplifyPath(path="/../"))
