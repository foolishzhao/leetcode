from typing import List

'''
you can disconnect any given island formation in at most 2 days.
i.e. Imagine a 30-by-30 array of all 1's. For the top left corner, remove the one to the right and below. you are done.
'''


class Solution:
    def connected(self, grid):
        def dfs(u, v):
            if 0 <= u < m and 0 <= v < n and grid[u][v] and (u, v) not in visited:
                visited.add((u, v))
                dfs(u + 1, v)
                dfs(u - 1, v)
                dfs(u, v + 1)
                dfs(u, v - 1)

        res, m, n = 0, len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    res += 1
                    if res > 1:
                        return False
                    dfs(i, j)
        return True

    def minDays(self, grid: List[List[int]]) -> int:
        if not self.connected(grid):
            return 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    if not self.connected(grid):
                        return 1
                    grid[i][j] = 1
        return 2
