from typing import List
import collections
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake = collections.defaultdict(list)
        for i, lk in enumerate(rains):
            if lk:
                lake[lk].append(i)

        pq = list()

        res, full = list(), set()
        for i, lk in enumerate(rains):
            if lk:
                if lk in full:
                    return []
                res.append(-1)
                full.add(lk)
                lake[lk].pop(0)
                if lake[lk]:
                    heapq.heappush(pq, (lake[lk][0], lk))
            else:
                if pq:
                    _, f = heapq.heappop(pq)
                    res.append(f)
                    full.remove(f)
                else:
                    res.append(1)
        return res
