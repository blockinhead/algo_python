class Solution:
    def totalNQueens(self, n: int) -> int:

        res = 0

        def place(row, cols, diag1, diag2):
            # в каждую строку можно поставить только одну королеву. если мы здесь, то решение найдено
            if row == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                # королеву можно поставить только в ту колонку, которая не под атакой других королев
                # под атакой две деиагонали. фокус в том, что у одной диагонали разность индексов - константа,
                # а у другой - сумма индексов - константа
                if c in cols or c - row in diag1 or c + row in diag2:
                    continue

                cols.add(c)
                diag1.add(c - row)
                diag2.add(c + row)
                place(row + 1, cols, diag1, diag2)
                cols.remove(c)
                diag1.remove(c - row)
                diag2.remove(c + row)

        place(0, set(), set(), set())

        return res
