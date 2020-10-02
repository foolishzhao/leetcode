from typing import List


# 二维叉积, cross product
# |a×b|=|a||b|sin(theta) = x1y2 - x2y1
# ||a×b||的值是以a，b为边构成平行四边形的面积
# if |a×b| < 0, then theta < 0, i.e. b go clockwise compared to a
# if |a×b| > 0, then theta > 0, i.e. b go anti-clockwise compared to a

# Monotone_Chain_Convex_Hull
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        if not points:
            return points

        points.sort(key=lambda x: (x[0], x[1]))

        lower = list()
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = list()
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # if some convex points are co-linear, they can both exist in upper and lower
        return list(map(list, set(map(tuple, lower + upper))))
