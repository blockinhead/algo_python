class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        low = 0
        high = len(digits) - 1
        while high >= low:
            if digits[high] != digits[low]:
                return False
            low += 1
            high -= 1

        return True
