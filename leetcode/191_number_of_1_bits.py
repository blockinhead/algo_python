class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for _ in range(32):
            counter += n % 2
            n = n >> 1

        return counter
