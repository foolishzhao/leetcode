import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        pq = [(0, 0, 0)]
        while pq:
            d, i, j = heapq.heappop(pq)
            if d < dist[i][j]:
                dist[i][j] = d
                for mov in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ni, nj = i + mov[0], j + mov[1]
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        continue

                    nd = max(dist[i][j], abs(heights[i][j] - heights[ni][nj]))
                    if nd < dist[ni][nj]:
                        heapq.heappush(pq, (nd, ni, nj))

        return dist[-1][-1]
