class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        res = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                res.append(end - start + 1)
                start, end = i + 1, i + 1

        return res
