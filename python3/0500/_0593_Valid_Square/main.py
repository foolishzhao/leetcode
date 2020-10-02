from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        def dot(o, x, y):
            return (x[0] - o[0]) * (y[0] - o[0]) + (x[1] - o[1]) * (y[1] - o[1])

        points = [p1, p2, p3, p4]
        points.sort(key=lambda x: (x[0], x[1]))

        return dist(points[0], points[1]) > 0 and \
               dist(points[0], points[1]) == \
               dist(points[0], points[2]) == \
               dist(points[3], points[1]) == \
               dist(points[3], points[2]) and \
               dot(points[0], points[1], points[2]) == \
               dot(points[1], points[0], points[3]) == \
               dot(points[2], points[0], points[3]) == \
               dot(points[3], points[1], points[2]) == 0
