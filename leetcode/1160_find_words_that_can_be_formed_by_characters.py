class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)

        res = 0
        for w in words:
            cw = Counter(w)
            for k, v in cw.items():
                if k not in counter:
                    break
                if counter[k] < v:
                    break
            else:
                res += len(w)

        return res
