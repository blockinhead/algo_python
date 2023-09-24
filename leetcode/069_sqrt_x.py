class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 1
        high = x // 2

        while low <= high:
            mid = (low + high) // 2

            if mid == x // mid:
                return mid

            if mid > x // mid:
                high = mid - 1
            else:
                low = mid + 1

        return high
