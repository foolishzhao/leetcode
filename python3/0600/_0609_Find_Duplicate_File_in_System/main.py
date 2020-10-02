from typing import List
import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dt = collections.defaultdict(list)
        for path in paths:
            ps = path.split(" ")
            d = ps[0]
            for p in ps[1:]:
                idx = p.find('(')
                dt[p[idx + 1: -1]].append(d + '/' + p[:idx])
        return [v for v in dt.values() if len(v) > 1]
