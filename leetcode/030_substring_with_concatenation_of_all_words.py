import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num_words = len(words)
        word_length = len(words[0])
        substring_length = num_words * word_length
        wd = collections.Counter(words)
        res = []

        for i in range(len(s) - substring_length + 1):
            ss = s[i:substring_length + i]
            current_counter = collections.defaultdict(int)
            for j in range(num_words):
                sss = ss[j*word_length: j * word_length + word_length]
                if sss not in wd:
                    break
                current_counter[sss] += 1
                if current_counter[sss] > wd[sss]:
                    break
            else:
                # else is not reached if cycle was breaked
                res.append(i)

        return res





print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
