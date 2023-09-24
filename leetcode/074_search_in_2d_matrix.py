from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        total = r * c

        first = 0
        last = total - 1

        while first <= last:

            mid = (first + last) // 2
            # print(f'{first=} {last=} {mid=}')
            _r, _c = mid // c , mid % c

            if target == matrix[_r][_c]:
                return True

            if target < matrix[_r][_c]:
                last = mid - 1
            else:
                first = mid + 1

        return False
