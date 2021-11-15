from typing import List
import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x: int(x), reverse=True)
        return nums[k - 1]

    def kthLargestNumber2(self, nums: List[str], k: int) -> str:
        pq = list()
        for x in nums:
            if len(pq) < k:
                heapq.heappush(pq, int(x))
            elif pq[0] < int(x):
                heapq.heappush(pq, int(x))
                heapq.heappop(pq)
        return str(pq[0])
