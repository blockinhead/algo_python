class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        prev_row_len = 2 ** (n - 2)
        if k <= prev_row_len:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - prev_row_len)


# 0
# 01
# 0110
# 01101001
# 0110100110010110
# 01101001100101101001011001101001
# первая половина такая же как в предыдущем ряду, вторая половина инвертирована
