from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        d = [float('inf')] * (amount + 1)
        d[0] = 0

        for i in range(1, amount + 1):
            if i in coins:
                d[i] = 1
                continue

            for c in coins:
                if i - c > 0:
                    d[i] = min(d[i], d[i - c] + 1)

        # print(d)

        if d[-1] != float('inf'):
            return d[-1]

        return -1
