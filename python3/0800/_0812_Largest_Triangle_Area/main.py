from typing import List
import math


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def dist(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def area(p1, p2, p3):
            a, b, c = dist(p1, p2), dist(p1, p3), dist(p2, p3)
            if a + b > c and a + c > b and b + c > a:
                return 0.25 * math.sqrt((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a))
            return 0

        res, n = 0, len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    res = max(res, area(points[i], points[j], points[k]))
        return res
