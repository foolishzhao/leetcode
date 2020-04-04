from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res += 1

        return res
