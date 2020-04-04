import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        z = sorted(zip(Profits, Capital), key=lambda x: x[1])

        pq, i = list(), 0
        while k:
            while i < len(z) and z[i][1] <= W:
                heapq.heappush(pq, -z[i][0])
                i += 1

            if not pq:
                break

            W -= heapq.heappop(pq)
            k -= 1

        return W
