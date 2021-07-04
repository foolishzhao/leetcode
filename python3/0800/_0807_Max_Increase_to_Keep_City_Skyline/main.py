from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rowMax, colMax = [max(row) for row in grid], [0] * n
        for i in range(n):
            mx = 0
            for j in range(m):
                mx = max(mx, grid[j][i])
            colMax[i] = mx

        return sum([min(rowMax[i], colMax[j]) - grid[i][j] for i in range(m) for j in range(n)])
