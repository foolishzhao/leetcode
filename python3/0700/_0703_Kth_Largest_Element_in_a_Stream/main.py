from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = list()
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
