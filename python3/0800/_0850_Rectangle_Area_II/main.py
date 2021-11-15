from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ys = sorted(set([y for _, y1, _, y2 in rectangles for y in (y1, y2)]))
        yIdx = {y: i for i, y in enumerate(ys)}
        count = [0] * len(ys)

        lines = list()
        for x1, y1, x2, y2 in rectangles:
            lines.append((x1, y1, y2, 1))
            lines.append((x2, y1, y2, -1))
        lines.sort()

        curX, curYSum, res = 0, 0, 0
        for x, y1, y2, sig in lines:
            # every time when encounter a new x, curYSum is the correct one
            res += (x - curX) * curYSum

            curX, curYSum = x, 0
            for i in range(yIdx[y1], yIdx[y2]):
                count[i] += sig

            for i in range(len(ys) - 1):
                curYSum += (ys[i + 1] - ys[i]) if count[i] else 0

        return res % (10 ** 9 + 7)
