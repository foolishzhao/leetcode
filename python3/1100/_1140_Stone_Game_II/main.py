from typing import List
import functools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i, m):
            if i >= n:
                return 0

            res, cur = float('-inf'), 0
            for j in range(1, 2 * m + 1):
                if i + j - 1 < n:
                    cur += piles[i + j - 1]
                    res = max(res, cur - dfs(i + j, max(m, j)))
            return res

        n = len(piles)
        return (sum(piles) + dfs(0, 1)) // 2

    # dp[i, m] = max stones current player can get from piles[i:] with m
    def stoneGameII2(self, piles: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return piles[i]
            return piles[i] - min(dp(i + j, max(m, j)) for j in range(1, 2 * m + 1))

        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        return dp(0, 1)
