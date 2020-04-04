from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for mi, mj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + mi, j + mj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n or not grid[ni][nj]:
                            res += 1
        return res
