from typing import List
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n, pq, res, i = len(apples), list(), 0, 0
        while i < n or pq:
            if i < n and apples[i] > 0:
                heapq.heappush(pq, [days[i] + i, apples[i]])

            while pq:
                d, a = heapq.heappop(pq)
                if d <= i:
                    continue
                if a > 1:
                    heapq.heappush(pq, [d, a - 1])
                res += 1
                break
            i += 1
        return res
