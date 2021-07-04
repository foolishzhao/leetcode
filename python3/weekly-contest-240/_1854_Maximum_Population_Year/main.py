from typing import List
import heapq


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()

        res, maxP, pq = 0, 0, list()
        for b, d in logs:
            heapq.heappush(pq, d - 1)
            while pq and pq[0] < b:
                heapq.heappop(pq)
            if len(pq) > maxP:
                maxP = len(pq)
                res = b
        return res

    def maximumPopulation2(self, logs: List[List[int]]) -> int:
        p = [0] * 2051
        for b, d in logs:
            p[b] += 1
            p[d] -= 1

        res, cur, maxP = 0, 0, 0
        for i in range(1950, 2051):
            cur += p[i]
            if cur > maxP:
                maxP = cur
                res = i
        return res
