class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0

        for i in range(len(points) - 1):
            x_distance = abs(points[i][0] - points[i + 1][0])
            y_distance = abs(points[i][1] - points[i + 1][1])
            res += min(x_distance, y_distance) + abs(x_distance - y_distance)

        return res
