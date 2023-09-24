from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] * len(digits)

        next_one = True

        for i in range(1, len(digits) + 1):
            i *= -1
            new_val = digits[i] + 1 if next_one else digits[i]
            # print(new_val)
            if new_val >= 10:
                res[i] = new_val % 10
                next_one = True
            else:
                res[i] = new_val
                next_one = False

        if next_one:
            return [1] + res
        return res
