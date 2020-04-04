from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.points = list()
        cur = 0
        # cache how many points, not area
        for x1, y1, x2, y2 in rects:
            cur += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.points.append(cur)

    def pick(self) -> List[int]:
        r = random.randint(1, self.points[-1])
        idx = bisect.bisect_left(self.points, r)
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]
