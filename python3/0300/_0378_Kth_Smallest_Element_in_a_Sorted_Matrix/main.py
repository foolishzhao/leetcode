from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = list()
        for j, num in enumerate(matrix[0]):
            heapq.heappush(pq, (num, 0, j))

        for i in range(k - 1):
            _, i, j = heapq.heappop(pq)
            if i + 1 < n:
                heapq.heappush(pq, (matrix[i + 1][j], i + 1, j))

        return pq[0][0]

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (high - low) // 2 + low
            count, j = 0, n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
