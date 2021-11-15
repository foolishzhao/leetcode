from typing import List
import collections


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dt = collections.defaultdict(int)
        for w, h in rectangles:
            dt[w / h] += 1
        return sum(v * (v - 1) // 2 for v in dt.values())
