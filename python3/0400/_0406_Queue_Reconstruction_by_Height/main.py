from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res, pq = list(), list()
        for h, k in people:
            heapq.heappush(pq, (-h, k))

        while pq:
            h, k = heapq.heappop(pq)
            res.insert(k, (-h, k))

        return res
