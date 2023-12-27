class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter(t)

        for l in s:
            if l not in d:
                return False

            if d[l] == 0:
                return False

            d[l] -= 1

        for l in d:
            if d[l] > 0:
                return False

        return True
