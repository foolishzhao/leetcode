from typing import List
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n, pq = len(arr), list()
        seen = {0}

        heapq.heappush(pq, (arr[0] / arr[-1], 0, n - 1))
        while k:
            _, i, j = heapq.heappop(pq)

            k -= 1
            if not k:
                return [arr[i], arr[j]]

            if i < j - 1:
                heapq.heappush(pq, (arr[i] / arr[j - 1], i, j - 1))

            if i + 1 < n - 1 and i + 1 not in seen:
                heapq.heappush(pq, (arr[i + 1] / arr[n - 1], i + 1, n - 1))
                seen.add(i + 1)
