from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, q = len(grid), [(0, 0)]
        seen = set(q)

        t = grid[0][0]
        while True:
            for (i, j) in q:
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= t and (ni, nj) not in seen:
                        if (ni, nj) == (n - 1, n - 1):
                            return t

                        seen.add((ni, nj))
                        q.append((ni, nj))
            t += 1

    def swimInWater2(self, grid: List[List[int]]) -> int:
        n, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], {(0, 0)}, 0

        while pq:
            t, i, j = heapq.heappop(pq)
            res = max(res, t)
            if i == j == n - 1:
                return res

            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    heapq.heappush(pq, (grid[ni][nj], ni, nj))
