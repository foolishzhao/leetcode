from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ks = [min(l, w) for l, w in rectangles]
        return ks.count(max(ks))
