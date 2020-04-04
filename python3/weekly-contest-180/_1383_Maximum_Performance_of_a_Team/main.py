from typing import List
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = [(s, e) for s, e in zip(speed, efficiency)]
        people.sort(key=lambda x: -x[1])

        pq = list()
        res, curSum = 0, 0
        for s, e in people:
            curSum += s
            heapq.heappush(pq, s)
            if len(pq) > k:
                curSum -= heapq.heappop(pq)

            res = max(res, e * curSum)

        return res % (10 ** 9 + 7)
