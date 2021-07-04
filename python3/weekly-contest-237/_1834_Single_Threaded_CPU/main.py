from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        inQ, outQ, res, availTime = list(), list(), list(), 0
        for i, task in enumerate(tasks):
            heapq.heappush(inQ, (task[0], i, task[1]))

        while inQ or outQ:
            if not outQ:
                et, index, pt = heapq.heappop(inQ)
                heapq.heappush(outQ, (pt, index, et))

                while inQ and inQ[0][0] == et:
                    et, index, pt = heapq.heappop(inQ)
                    heapq.heappush(outQ, (pt, index, et))

            pt, index, et = heapq.heappop(outQ)
            res.append(index)

            availTime = max(et, availTime) + pt
            while inQ and inQ[0][0] <= availTime:
                et, index, pt = heapq.heappop(inQ)
                heapq.heappush(outQ, (pt, index, et))
        return res
