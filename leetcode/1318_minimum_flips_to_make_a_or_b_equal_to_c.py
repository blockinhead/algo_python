class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        res = 0

        for _ in range(32):
            a_ = a & 1
            b_ = b & 1
            c_ = c & 1

            # if c_ == 1 and ((a_ & b_) != 1):
            #     res += 1
            # if c_ == 0 and ((a_ & b_) == 1):
            #     res += 2
            if c_ == 1:
                if a_ == 1 or b_ == 1:
                    pass
                else:
                    res += 1
            else:  # c_ == 0
                if a_ == 1:
                    if b_ == 1:
                        res += 2
                    else:
                        res += 1
                else:  # a_ == 0
                    if b_ == 1:
                        res += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return res
