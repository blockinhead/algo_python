class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        is_negative = True if x < 0 else False
        x = abs(x)

        while x != 0:
            digit = x % 10
            res  = res * 10 + digit
            x = x // 10

        res = -res if is_negative else res

        maximum = 2**31
        if -maximum <= res < maximum:
            return res

        return 0
    