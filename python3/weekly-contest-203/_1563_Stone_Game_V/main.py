from typing import List
import functools


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            res = 0
            for k in range(i, j):
                ls = prefix[k + 1] - prefix[i]
                rs = prefix[j + 1] - prefix[k + 1]
                if ls >= rs:
                    res = max(res, dp(k + 1, j) + rs)
                if rs >= ls:
                    res = max(res, dp(i, k) + ls)
            return res

        return dp(0, n - 1)
