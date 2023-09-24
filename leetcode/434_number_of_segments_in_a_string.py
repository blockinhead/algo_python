class Solution:
    def countSegments(self, s: str) -> int:
        counter = 0
        word = False

        for c in s:
            if not word and c == ' ':
                continue
            if not word and c != ' ':
                word = True
                continue
            if word and c == ' ':
                word = False
                counter += 1
                continue
            if word and c != ' ':
                continue

        if word:
            counter += 1

        return counter
