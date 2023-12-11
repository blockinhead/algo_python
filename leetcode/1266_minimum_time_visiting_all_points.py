class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            x = abs(p2[0] - p1[0])
            y = abs(p2[1] - p1[1])
            diag = min(x, y)
            strait = max(x, y) - diag
            return diag + strait

        return sum(map(lambda p: dist(p[0], p[1]), zip(points, points[1:])))
