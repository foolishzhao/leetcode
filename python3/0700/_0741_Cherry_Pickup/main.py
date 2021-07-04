import functools
from typing import List


class Solution:
    # assume depart from 0, 0 with two paths to the destination
    # then x1 + y1 == x2 + y2 will always be true
    # and for (x1, y1) achieved at time t, (x2, y2) can never achieve this point except time t
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(x1, y1, x2, y2):
            if x1 == n or y1 == n or x2 == n or y2 == n:
                return -1
            if x1 == n - 1 and y1 == n - 1 and x2 == n - 1 and y2 == n - 1:
                return grid[x1][y1]
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -1

            res = max(dp(x1 + 1, y1, x2 + 1, y2),
                      dp(x1 + 1, y1, x2, y2 + 1),
                      dp(x1, y1 + 1, x2 + 1, y2),
                      dp(x1, y1 + 1, x2, y2 + 1))
            if res != -1:
                if x1 == x2 and y1 == y2:
                    res += grid[x1][y1]
                else:
                    res += grid[x1][y1] + grid[x2][y2]
            return res

        n = len(grid)
        return max(dp(0, 0, 0, 0), 0)
