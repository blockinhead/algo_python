from typing import List




def letterCasePermutation(self, s: str) -> List[str]:
    i = 0
    res = []
    while i < len(s):
        if s[i].isalpha():
            res += [s[:i+1].lower() + v for v in letterCasePermutation(None, s[i + 1:])]
            res += [s[:i+1].upper() + v for v in letterCasePermutation(None, s[i + 1:])]
            break

        i+=1

    if i == len(s):
        return [s]

    return res

print(letterCasePermutation(None, 'a1b2'))