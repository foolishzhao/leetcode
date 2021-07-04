from typing import List
import functools


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        @functools.lru_cache(None)
        def dp(t, x1, y1, x2, y2):
            if t == r * c * 2 or (x1 == x2 and y1 == y2) or grid[x2][y2] == 'F':
                return False

            if grid[x1][y1] == 'F':
                return True

            if t % 2 == 0:  # mouse move
                for dx, dy in dirs:
                    for jump in range(mouseJump + 1):  # can stay at same position
                        nx1, ny1 = x1 + dx * jump, y1 + dy * jump
                        if nx1 < 0 or nx1 >= r or ny1 < 0 or ny1 >= c or grid[nx1][ny1] == '#':
                            break

                        if dp(t + 1, nx1, ny1, x2, y2):
                            return True
                return False
            else:  # cat move
                for dx, dy in dirs:
                    for jump in range(catJump + 1):  # can stay at same position
                        nx2, ny2 = x2 + dx * jump, y2 + dy * jump
                        if nx2 < 0 or nx2 >= r or ny2 < 0 or ny2 >= c or grid[nx2][ny2] == '#':
                            break

                        if not dp(t + 1, x1, y1, nx2, ny2):
                            return False
                return True

        r, c, cr, cc, mr, mc = len(grid), len(grid[0]), 0, 0, 0, 0
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'C':
                    cr, cc = i, j
                if grid[i][j] == 'M':
                    mr, mc = i, j
        return dp(0, mr, mc, cr, cc)


if __name__ == '__main__':
    print(Solution().canMouseWin(
        ["####.##", ".#C#F#.", "######.", "##M.###"],
        3,
        6,
    ))
