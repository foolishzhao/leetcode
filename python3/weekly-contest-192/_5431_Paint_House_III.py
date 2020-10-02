import functools
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # houses[i] is painted with v
        # use houses[:i + 1] to achieve target j
        # as neighborhood definition, don't need care houses val in houses[i + 1:]
        @functools.lru_cache(None)
        def dp(i, v, j):
            if i == 0:
                return 0 if j == 1 else -1

            if j > i + 1:
                return -1

            res = float('inf')
            # houses[i - 1] == houses[i]
            if houses[i - 1] == v:
                if dp(i - 1, v, j) != -1:
                    res = min(res, dp(i - 1, v, j))
            elif houses[i - 1] == 0 and v != n + 1 and dp(i - 1, v, j) != -1:
                res = min(res, dp(i - 1, v, j) + cost[i - 1][v - 1])

            # houses[i - 1] != houses[i]
            if houses[i - 1]:
                if houses[i - 1] != v and dp(i - 1, houses[i - 1], j - 1) != -1:
                    res = min(res, dp(i - 1, houses[i - 1], j - 1))
            else:
                for t in range(1, n + 1):
                    if t != v and dp(i - 1, t, j - 1) != -1:
                        res = min(res, dp(i - 1, t, j - 1) + cost[i - 1][t - 1])

            return -1 if res == float('inf') else res

        return dp(m, n + 1, target + 1)
