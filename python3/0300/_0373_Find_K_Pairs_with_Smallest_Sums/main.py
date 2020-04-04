from typing import List
import heapq


class Solution:
    # Time complexity: O(m * n *log(k)), Space complexity: O(k)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(pq, (-n1 - n2, [n1, n2]))
                if len(pq) > k:
                    heapq.heappop(pq)

        return [x[1] for x in pq]

    # Time complexity: O(k*log(k)), Space complexity: O(k)
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        pq, res = [], []
        m, n = len(nums1), len(nums2)
        for i in range(min(m, k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))

        while pq and len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])

            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
