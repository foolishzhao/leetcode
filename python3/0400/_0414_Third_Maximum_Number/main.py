from typing import List
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pq = list()
        for num in nums:
            if num not in pq:
                if len(pq) < 3:
                    heapq.heappush(pq, num)
                elif pq[0] < num:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)

        return pq[0] if len(pq) == 3 else max(pq)
