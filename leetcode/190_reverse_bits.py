class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(31):
            last_bit = n % 2
            res += last_bit

            n = n >> 1
            res = res << 1

        res += n

        return res
