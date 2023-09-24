class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prev_letters = {}
        prev_comb_start = 0
        for i in range(len(s)):
            current_letter = s[i]
            if current_letter not in prev_letters:
                prev_letters[current_letter] = i
                continue

            new_res = i - prev_comb_start
            if res < new_res:
                res = new_res
            new_prev_comb_start = prev_letters[current_letter] + 1
            if new_prev_comb_start > prev_comb_start:
                prev_comb_start = new_prev_comb_start
            prev_letters[current_letter] = i

        new_res = len(s) - prev_comb_start
        if res < new_res:
            res = new_res

        return res
