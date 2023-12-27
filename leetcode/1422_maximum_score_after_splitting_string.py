class Solution:
    def maxScore(self, s: str) -> int:
        cou = Counter(s)

        first = int(s[0])
        left_zeroes = 1 - first
        score = left_zeroes + cou['1'] - first
        right_ones = cou['1'] - first

        for c in s[1:-1]:
            if c == '1':
                right_ones -= 1
            else:
                left_zeroes += 1

            score = max(score, left_zeroes + right_ones)

        return score
