from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        char = ''
        num = 0
        pos = 0

        for c in chars:
            if c == char:
                num += 1
                continue

            if num == 0:
                char = c
                num += 1
            elif num == 1:
                chars[pos] = char
                char = c
                num = 1
                pos += 1
            else:
                chars[pos] = char
                pos += 1
                for n in '%d' % num:
                    chars[pos] = n
                    pos += 1
                char = c
                num = 1

        if num == 1:
            chars[pos] = char
            pos += 1
        else:
            chars[pos] = char
            pos += 1
            for n in '%d' % num:
                chars[pos] = n
                pos += 1

        return pos
