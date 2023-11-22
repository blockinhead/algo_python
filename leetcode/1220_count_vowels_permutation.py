from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        vowels = dict(a=('e', ),
                e=('a', 'i',),
                i=('a', 'e', 'o', 'u', ),
                o=('i', 'u',),
                u=('a',))

        @cache
        def dive(letter, length):
            if not length:
                return 1

            num_vars = 0
            for next_letter in vowels[letter]:
                num_vars += dive(next_letter, length - 1)

            return num_vars % mod

        return sum(dive(l, n - 1) for l in vowels) % mod



print(Solution().countVowelPermutation(2))
