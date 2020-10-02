from typing import List
import math


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dis(cx, cy):
            return sum([math.sqrt((x - cx) ** 2 + (y - cy) ** 2) for x, y in positions])

        x = sum([x for x, y in positions]) / len(positions)
        y = sum([y for x, y in positions]) / len(positions)
        res, step = dis(x, y), 100
        while step > 1e-6:
            zoom = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + step * dx, y + step * dy
                nd = dis(nx, ny)
                if nd < res:
                    res = nd
                    x, y = nx, ny
                    zoom = False
            if zoom:
                step /= 2
        return res
