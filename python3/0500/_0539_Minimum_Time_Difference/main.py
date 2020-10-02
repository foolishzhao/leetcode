from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [x.split(":") for x in timePoints]
        points = sorted([(int(x), int(y)) for x, y in timePoints])
        points.append((points[0][0] + 24, points[0][1]))

        res = float('inf')
        for x, y in zip(points[:-1], points[1:]):
            res = min(res, (y[0] - x[0]) * 60 + y[1] - x[1])
        return res

    def findMinDifference2(self, timePoints: List[str]) -> int:
        points = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timePoints])
        points.append(points[0] + 24 * 60)

        res = float('inf')
        for x, y in zip(points[:-1], points[1:]):
            res = min(res, y - x)
        return res
