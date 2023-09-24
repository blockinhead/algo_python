class Solution:
    def intToRoman(self, num: int) -> str:
        s_to_v = {1: 'I',
                  4: 'IV',
                  5: 'V',
                  9: 'IX',
                  10: 'X',
                  40: 'XL',
                  50: 'L',
                  90: 'XC',
                  100: 'C',
                  400: 'CD',
                  500: 'D',
                  900: 'CM',
                  1000: 'M'}
        res = ''
        keys = list(s_to_v.keys())
        keys.reverse()

        while num != 0:
            for k in keys:
                if (rest := num - k) >= 0:
                    res += s_to_v[k]
                    num = rest
                    break

        return res


print(Solution().intToRoman(1994))
print(Solution().intToRoman(58))
