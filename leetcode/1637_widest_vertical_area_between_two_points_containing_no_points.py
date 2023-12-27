class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        m = 0
        points.sort()
        for i in range(1, len(points)):
            m = max(m, points[i][0] - points[i - 1][0])
        return m
