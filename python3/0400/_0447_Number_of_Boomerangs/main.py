from typing import List
import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n, res = len(points), 0
        for i in range(n):
            dt = collections.defaultdict(int)
            for j in range(n):
                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                dt[dist] += 1

            for dist, count in dt.items():
                res += count * (count - 1)

        return res
