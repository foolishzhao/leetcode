from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def bfs(u, v):
            q, area = [(u, v)], 0
            while q:
                x, y = q.pop(0)
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    grid[x][y] = 0
                    area += 1
                    q.append((x + 1, y))
                    q.append((x - 1, y))
                    q.append((x, y + 1))
                    q.append((x, y - 1))
            return area

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, bfs(i, j))
        return res

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(u, v):
            if 0 <= u < m and 0 <= v < n and grid[u][v]:
                grid[u][v] = 0
                return 1 + dfs(u + 1, v) + dfs(u - 1, v) + dfs(u, v + 1) + dfs(u, v - 1)
            return 0

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res
