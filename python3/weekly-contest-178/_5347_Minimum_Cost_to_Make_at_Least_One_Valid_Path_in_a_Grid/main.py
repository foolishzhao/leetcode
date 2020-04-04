from typing import List
import heapq


class Solution:
    # Time complexity: O(mn*log(mn))
    # Space complexity: O(mn)
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        pq = list([(0, 0, 0)])
        while pq:
            c, i, j = heapq.heappop(pq)
            for d, mov in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
                ni, nj = i + mov[0], j + mov[1]
                if 0 <= ni < m and 0 <= nj < n:
                    nc = c if grid[i][j] == d + 1 else c + 1
                    if nc < dist[ni][nj]:
                        dist[ni][nj] = nc
                        heapq.heappush(pq, (nc, ni, nj))

        return dist[-1][-1]

    def minCost2(self, grid: List[List[int]]) -> int:
        m, n, cost = len(grid), len(grid[0]), 0
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [[float('inf')] * n for _ in range(m)]
        q = list()

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and dist[x][y] == float('inf'):
                q.append((x, y))
                dist[x][y] = cost
                dfs(x + ds[grid[x][y] - 1][0], y + ds[grid[x][y] - 1][1])

        dfs(0, 0)
        while q:
            cost += 1
            sz = len(q)
            for _ in range(sz):
                x, y = q.pop(0)
                for dx, dy in ds:
                    dfs(x + dx, y + dy)

        return dist[-1][-1]


if __name__ == '__main__':
    Solution().minCost2([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]])
