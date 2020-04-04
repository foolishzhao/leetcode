from typing import List


class Solution:
    def __init__(self):
        self.dt = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        return self.dfs(grid, 0, 0, m, n, set())

    def dfs(self, grid, i, j, m, n, visited):
        if i == m - 1 and j == n - 1:
            return True

        # no need to remove from visited, coz if (i, j) can't find a path, no need to dfs it again.
        visited.add((i, j))
        for x, y in self.dt[grid[i][j]]:
            ni, nj = i + x, j + y
            # a connects b requires a can get to b and b can get to a
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and (-x, -y) in self.dt[grid[ni][nj]]:
                if self.dfs(grid, ni, nj, m, n, visited):
                    return True
        return False
