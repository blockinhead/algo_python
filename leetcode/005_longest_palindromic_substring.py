class Solution:
    def longestPalindrome(self, s: str) -> str:
        m_len = float('-inf')
        start = 0
        end = 0

        for i in range(1, len(s)):

            # проверяем, не является ли полиндромом подстрока, центра которой в и-1 и (четная длинная)
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if m_len < high - low:
                    m_len = high - low
                    start = low
                    end = high
                low -= 1
                high += 1

            # проверяем, не является ли полиндромом подстрака с серединой в и (нечётная длинна)
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if m_len < high - low:
                    m_len = high - low
                    start = low
                    end = high
                low -= 1
                high += 1

        return s[start: end + 1]
