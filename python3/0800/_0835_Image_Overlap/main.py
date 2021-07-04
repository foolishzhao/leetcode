from typing import List
import collections


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1 = [(i, j) for i, row in enumerate(img1) for j, x in enumerate(row) if x]
        img2 = [(i, j) for i, row in enumerate(img2) for j, x in enumerate(row) if x]

        dt = collections.defaultdict(int)
        for i1, j1 in img1:
            for i2, j2 in img2:
                dt[(i1 - i2, j1 - j2)] += 1

        return max(dt.values()) if dt else 0
