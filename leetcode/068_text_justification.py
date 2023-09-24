from typing import List
from math import ceil


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_counter = 0
        cache = []
        res = []
        while words_counter < len(words):
            # add first word to empty cache
            cache.append(words[words_counter])
            current_cache_len = len(words[words_counter])
            words_counter += 1

            while words_counter < len(words) and current_cache_len + 1 + len(words[words_counter]) <= maxWidth:
                cache.append(words[words_counter])
                current_cache_len += 1 + len(words[words_counter])  # 1 is for space between prev word and current word
                words_counter += 1

            res.append(cache)
            cache = []

        for i in range(len(res) - 1):
            reminder = maxWidth - sum([len(x) for x in res[i]])
            if len(res[i]) == 1:
                res[i] = res[i][0] + ' ' * int(reminder)
                continue

            s = ''
            for j, w in enumerate(res[i][:-1]):
                space_to_insers = reminder / (len(res[i]) - 1 - j)
                s += w + ' ' * ceil(space_to_insers)
                reminder -= ceil(space_to_insers)
            s += res[i][-1]

            res[i] = s

        s = ' '.join(res[-1])
        res[-1] = s + ' ' * (maxWidth - len(s))

        return res




# print(Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
# print(Solution().fullJustify(words=["everything","else","we","do"], maxWidth = 20))
print(Solution().fullJustify(words=["What","must","be","acknowledgment","shall","be"], maxWidth=16))
