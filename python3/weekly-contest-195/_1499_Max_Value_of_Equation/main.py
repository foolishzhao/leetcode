from typing import List
import heapq
import collections


class Solution:
    # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res, pq = float('-inf'), list()
        for x, y in points:
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                res = max(res, x + y - pq[0][0])
            heapq.heappush(pq, (-(y - x), x))
        return res

    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        res, dq = float('-inf'), collections.deque()
        for x, y in points:
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                res = max(res, x + y + dq[0][1] - dq[0][0])
            while dq and dq[-1][1] - dq[-1][0] <= y - x:
                dq.pop()
            dq.append((x, y))
        return res
