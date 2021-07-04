from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[min(i, j, N - 1 - i, N - 1 - j) + 1 for i in range(N)] for j in range(N)]
        for x, y in mines:
            for i in range(N):
                grid[i][y] = min(grid[i][y], abs(i - x))
                grid[x][i] = min(grid[x][i], abs(i - y))
        return max(max(row) for row in grid)

    def orderOfLargestPlusSign2(self, N: int, mines: List[List[int]]) -> int:
        grid = [[N] * N for _ in range(N)]
        for x, y in mines:
            grid[x][y] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] else 0
                grid[i][j] = min(grid[i][j], l)

                u = u + 1 if grid[j][i] else 0
                grid[j][i] = min(grid[j][i], u)

                r = r + 1 if grid[i][k] else 0
                grid[i][k] = min(grid[i][k], r)

                d = d + 1 if grid[k][i] else 0
                grid[k][i] = min(grid[k][i], d)

        return max(max(r) for r in grid)
