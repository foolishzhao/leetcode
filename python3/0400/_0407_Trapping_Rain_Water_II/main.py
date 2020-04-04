from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n, res = len(heightMap), len(heightMap[0]), 0

        visited = [[False] * n for _ in range(m)]
        pq = list()
        for i in range(m):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True

        for j in range(1, n - 1):
            heapq.heappush(pq, (heightMap[0][j], 0, j))
            heapq.heappush(pq, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True

        while pq:
            h, i, j = heapq.heappop(pq)
            for mi, mj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + mi, j + mj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    res += max(h - heightMap[ni][nj], 0)
                    heapq.heappush(pq, (max(h, heightMap[ni][nj]), ni, nj))

        return res
