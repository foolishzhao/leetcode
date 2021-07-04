from typing import List
import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pq, res = list(), 0
        for d, p in zip(difficulty, profit):
            heapq.heappush(pq, (-p, d))

        worker.sort()
        for w in worker[::-1]:
            while pq and pq[0][1] > w:
                heapq.heappop(pq)

            if not pq:
                break

            res -= pq[0][0]

        return res
