from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        bad_columns = set()
        good_columns = set()
        for row in mat:
            ones = [c for c, v in enumerate(row) if v == 1]
            if not ones:
                continue
            if len(ones) > 1:
                bad_columns.update(ones)
                good_columns -= bad_columns
                continue
            c = ones[0]
            if c in bad_columns:
                bad_columns.add(c)
                continue
            if c in good_columns:
                bad_columns.add(c)
                good_columns.remove(c)
                continue
            good_columns.add(c)

        return len(good_columns)


# print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print(Solution().numSpecial([[0,0,0,0,0,0,0,0],
                             [0,0,0,1,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,1,0],
                             [0,1,0,0,0,0,1,0],
                             [0,1,0,0,0,0,0,0]]))