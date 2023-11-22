from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def build_solution(poses):
            r = []
            for p in poses:
                t = ['.'] * n
                t[p] = 'Q'
                r.append(''.join(t))
            res.append(r)

        def place(row, cols, diags1, diags2, poses):
            if row == n:
                build_solution(poses)
                return

            for c in range(n):
                if c in cols or c - row in diags1 or c + row in diags2:
                    continue
                poses.append(c)
                cols.add(c)
                diags1.add(c - row)
                diags2.add(c + row)
                place(row + 1, cols, diags1, diags2, poses)
                poses.pop()
                cols.remove(c)
                diags1.remove(c - row)
                diags2.remove(c + row)

        place(0, set(), set(), set(), [])
        return res


# главный фокус - ряд ± колонка - константа для диагонали
