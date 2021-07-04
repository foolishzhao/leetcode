from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rotate(i, j, r, c, ne):
            nk = k % ne
            while nk:
                p1 = grid[i][j]

                for u in range(j, j + c - 1):
                    grid[i][u] = grid[i][u + 1]

                for v in range(i, i + r - 1):
                    grid[v][j + c - 1] = grid[v + 1][j + c - 1]

                for u in range(j + c - 1, j, -1):
                    grid[i + r - 1][u] = grid[i + r - 1][u - 1]

                for v in range(i + r - 1, i, -1):
                    grid[v][j] = grid[v - 1][j]

                grid[i + 1][j] = p1

                nk -= 1

        m, n = len(grid), len(grid[0])
        layer = min(m // 2, n // 2)

        for l in range(layer):
            r, c = m - 2 * l, n - 2 * l
            rotate(l, l, r, c, 2 * r + 2 * c - 4)
        return grid
