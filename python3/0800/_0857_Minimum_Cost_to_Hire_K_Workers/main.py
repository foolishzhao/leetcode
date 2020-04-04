from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        wpq = [(w / q, q) for q, w in zip(quality, wage)]
        wpq.sort()

        res, curQSum = float('inf'), 0
        pq = list()
        for w, q in wpq:
            curQSum += q
            heapq.heappush(pq, -q)
            if len(pq) == K:
                res = min(res, w * curQSum)
                curQSum += heapq.heappop(pq)

        return res
