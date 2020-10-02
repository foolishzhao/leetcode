from typing import List
import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq = list()
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > 2:
                heapq.heappop(pq)

        return (pq[0] - 1) * (pq[1] - 1)
