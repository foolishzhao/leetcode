from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        lo, hi = 1, 10 ** 7
        while lo <= hi:
            mi = (hi - lo) // 2 + lo
            time = sum([math.ceil(d / mi) for d in dist[:-1]]) + dist[-1] / mi
            if time <= hour:
                hi = mi - 1
            else:
                lo = mi + 1

        return lo
