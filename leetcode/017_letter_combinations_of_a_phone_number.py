from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []

        def dive(digits_, current_variant):
            # print(f'dive {digits_} {current_variant}')
            if not digits_:
                res.append(current_variant)
                return

            for l in d[digits_[0]]:
                new_variant = current_variant + l
                dive(digits_[1:], new_variant)

        dive(digits, '')

        return res
