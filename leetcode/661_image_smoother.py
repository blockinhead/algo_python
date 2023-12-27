class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def conv(i, j):
            t = c = 0
            for i_ in (i - 1, i, i + 1):
                for j_ in (j - 1, j, j + 1):
                    if 0 <= i_ < m and 0 <= j_ < n:
                        t += img[i_][j_]
                        c += 1

            return t // c

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = conv(i, j)

        return res
