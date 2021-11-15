import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = list()
        for p in piles:
            heapq.heappush(pq, -p)

        while k:
            p = heapq.heappop(pq)
            np = -p - (-p // 2)
            heapq.heappush(pq, -np)
            k -= 1

        return -sum(pq)
