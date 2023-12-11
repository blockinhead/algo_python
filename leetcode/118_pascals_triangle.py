class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for n_row in range(1, numRows):
            r = [1]
            p = res[-1]
            for i in range(1, n_row):
                r.append(p[i-1] + p[i])
            r.append(1)
            res.append(r)

        return res
