from typing import List
import functools


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(s, e):
            if e - s <= 1:
                return 0

            res = float('inf')
            for i in range(s + 1, e):
                res = min(res, dp(s, i) + dp(i, e) + cuts[e] - cuts[s])
            return res

        cuts = sorted([0] + cuts + [n])
        return dp(0, len(cuts) - 1)
