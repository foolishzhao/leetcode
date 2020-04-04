from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1

        return res

    def dfs(self, grid: List[List[str]], x: int, y: int) -> None:
        m, n = len(grid), len(grid[0])
        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
            grid[x][y] = '0'
            self.dfs(grid, x + 1, y)
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x, y + 1)
            self.dfs(grid, x, y - 1)
