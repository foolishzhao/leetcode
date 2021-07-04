from typing import List
import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dt = collections.defaultdict(list)
        for x, y in adjacentPairs:
            dt[x].append(y)
            dt[y].append(x)

        prev, cur = None, None
        for x in dt.keys():
            if len(dt[x]) == 1:
                cur = x
                break

        res = list()
        while cur is not None:  # corner case: cur equals to 0
            res.append(cur)

            nxt = None
            for x in dt[cur]:
                if x != prev:
                    nxt = x
            prev, cur = cur, nxt
        return res
