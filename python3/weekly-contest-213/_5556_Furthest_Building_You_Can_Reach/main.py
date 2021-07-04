from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, i, pq = len(heights), 1, list()
        while i < n:
            if heights[i] > heights[i - 1]:
                heapq.heappush(pq, heights[i] - heights[i - 1])
                if len(pq) > ladders:
                    if bricks >= pq[0]:
                        bricks -= heapq.heappop(pq)
                    else:
                        break
            i += 1
        return i - 1
