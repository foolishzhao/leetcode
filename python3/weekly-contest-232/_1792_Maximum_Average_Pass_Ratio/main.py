from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def ratioDelta(p, t):
            return (t * (p + 1) - p * (t + 1)) / (t * (t + 1))

        pq = list()
        for p, t in classes:
            heapq.heappush(pq, (-ratioDelta(p, t), p, t))

        while extraStudents:
            delta, p, t = heapq.heappop(pq)
            heapq.heappush(pq, (-ratioDelta(p + 1, t + 1), p + 1, t + 1))
            extraStudents -= 1

        return sum([p / t for _, p, t in pq]) / len(pq)
