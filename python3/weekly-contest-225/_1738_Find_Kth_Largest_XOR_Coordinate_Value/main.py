from typing import List
import heapq


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor = [[0] * (n + 1) for _ in range(m + 1)]
        pq = list()
        for i in range(m):
            for j in range(n):
                xor[i + 1][j + 1] = xor[i][j + 1] ^ xor[i + 1][j] ^ xor[i][j] ^ matrix[i][j]
                heapq.heappush(pq, -xor[i + 1][j + 1])

        while k > 1:
            heapq.heappop(pq)
            k -= 1

        return -pq[0]
