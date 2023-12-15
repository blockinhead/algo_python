class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()
        dst = set()

        for f, t in paths:
            src.add(f)
            if f in dst:
                dst.remove(f)
            if t not in src:
                dst.add(t)

        return list(dst)[0]
