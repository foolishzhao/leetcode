import heapq
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        pq = list()
        for d, s in zip(dist, speed):
            heapq.heappush(pq, d / s)

        t = 0
        while pq:
            curT = heapq.heappop(pq)
            if curT <= t:
                break

            t += 1
        return t
