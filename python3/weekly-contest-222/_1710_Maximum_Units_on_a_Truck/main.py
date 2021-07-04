from typing import List
import heapq


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for box, unit in boxTypes:
            while box and truckSize:
                box -= 1
                truckSize -= 1
                res += unit
        return res

    def maximumUnits2(self, boxTypes: List[List[int]], truckSize: int) -> int:
        pq = list()
        for box, unit in boxTypes:
            heapq.heappush(pq, (-unit, box))

        res = 0
        while pq and truckSize:
            unit, box = heapq.heappop(pq)
            if box <= truckSize:
                res -= box * unit
                truckSize -= box
            else:
                res -= truckSize * unit
                truckSize = 0
        return res
