from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(u, v):
            q = [(u, v)]
            while q:
                u, v = q.pop(0)
                if 0 <= u < m and 0 <= v < n and grid[u][v] == '1':
                    grid[u][v] = '0'
                    q.append((u + 1, v))
                    q.append((u - 1, v))
                    q.append((u, v + 1))
                    q.append((u, v - 1))

        def dfs(u, v):
            if 0 <= u < m and 0 <= v < n and grid[u][v] == '1':
                grid[u][v] = '0'
                dfs(u + 1, v)
                dfs(u - 1, v)
                dfs(u, v + 1)
                dfs(u, v - 1)

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
