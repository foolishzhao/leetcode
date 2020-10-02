from typing import List
import collections


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dt = collections.defaultdict(str)
        for x, y in paths:
            dt[x] = y

        for v in dt.values():
            if v not in dt:
                return v
