from typing import List
import functools


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(row, col_mask):
            res = 0 if row == m else float('inf')
            if row == m:
                for j in range(n):
                    if not (col_mask & (1 << j)):
                        res += minCol[j]
            else:
                for j in range(n):
                    res = min(res, cost[row][j] + dp(row + 1, col_mask | (1 << j)))
            return res

        m, n = len(cost), len(cost[0])
        minCol = [min([cost[i][j] for i in range(m)]) for j in range(n)]
        return dp(0, 0)
