from typing import List
import heapq


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1

        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            return self.minOperations(nums2, nums1)

        diff, pq, res = s2 - s1, list(), 0
        for num in nums1:
            heapq.heappush(pq, num - 6)
        for num in nums2:
            heapq.heappush(pq, 1 - num)

        while diff:
            t = heapq.heappop(pq)
            operation = min(diff, -t)
            diff -= operation
            res += 1
            if operation + t < 0:
                heapq.heappush(pq, operation + t)
        return res
