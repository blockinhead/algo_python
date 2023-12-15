class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                s = mul + res[p2]

                d, m = divmod(s, 10)
                res[p1] += d
                res[p2] = m

        return ''.join(map(str, res)).lstrip('0') or '0'
